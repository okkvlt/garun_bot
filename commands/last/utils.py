import sqlite3
from hashlib import md5

import discord
import requests
from bot import bot
from conf import API_KEY, API_SECRET, DB


def insert_session(id, last_user, session_key):
    c = sqlite3.connect(DB)
    ex = c.cursor()

    try:
        ex.execute("INSERT INTO users VALUES ("+str(id)+", '" +
                   last_user+"', '"+session_key+"', 0)")
    except Exception as error:
        return error

    c.commit()
    c.close()

    return 1


def get_users():
    c = sqlite3.connect(DB)
    ex = c.cursor()

    try:
        rows = ex.execute("SELECT * FROM users")
        users = rows.fetchall()

        c.commit()
        c.close()

        return users
    except Exception as error:
        return str(error)


def get_scrobblers():
    c = sqlite3.connect(DB)
    ex = c.cursor()

    try:
        users = {}

        rows = ex.execute("SELECT * FROM users WHERE scrobbling = 1")
        data = rows.fetchall()

        for user in data:
            users[user[0]] = user[1]

        c.commit()
        c.close()

        return users
    except Exception as error:
        return str(error)


def check_auth_sessions(id, mode):
    c = sqlite3.connect(DB)
    ex = c.cursor()

    users = get_users()

    count = 0
    check = 0

    for user in users:
        if id == user[0]:
            check = 1
            break
        count += 1

    c.commit()
    c.close()

    if mode == 1:
        return check
    else:
        return count


def get_token():
    r = requests.get(
        "https://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key="+API_KEY+"&format=json")

    return r.json()["token"]


def get_signature(params):
    sorted_params = sorted(params)

    string = ""

    for param in sorted_params:
        string += param+params[param]

    string += API_SECRET

    sig = md5(string.encode()).hexdigest()

    return sig


def get_session(token, sig):
    r = requests.get(
        "https://ws.audioscrobbler.com/2.0/?method=auth.getSession&api_key="+API_KEY+"&token="+token+"&api_sig="+sig+"&format=json")

    return r.json()


def get_topArtists(user, n, time):
    r = requests.get("https://ws.audioscrobbler.com/2.0/?method=user.gettopartists&user=" +
                     user+"&api_key="+API_KEY+"&limit="+n+"&period="+time+"&format=json")

    return r.json()


def get_topAlbums(user, n, time):
    r = requests.get("https://ws.audioscrobbler.com/2.0/?method=user.gettopalbums&user=" +
                     user+"&api_key="+API_KEY+"&limit="+n+"&period="+time+"&format=json")

    return r.json()


def getEmbed():
    embed = discord.Embed(colour=0xedd58d)

    embed.set_author(name="Garun — Last.fm",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    embed.set_footer(
        text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

    return embed


def scrobbleTrack(id_dict, artist, track, time):
    c = sqlite3.connect(DB)
    ex = c.cursor()

    if len(id_dict) > 0:
        done = []
        fail = []

        for session in id_dict:
            id = session
            acc = id_dict[session]

            count = check_auth_sessions(id, 2)

            try:
                rows = ex.execute("SELECT * FROM users")
                users = rows.fetchall()
            except Exception as error:
                return str(error)

            sk = users[count][2]

            data = {"artist": artist,
                    "track": track,
                    "timestamp": str(time),
                    "method": "track.scrobble",
                    "api_key": API_KEY,
                    "sk": sk}

            sig = get_signature(data)

            data["timestamp"] = time
            data["api_sig"] = sig

            r = requests.post("http://ws.audioscrobbler.com/2.0/", data=data)

            embed_last = getEmbed()

            c.commit()
            c.close()

            if 'accepted="1"' in r.text:
                done.append(acc)
            else:
                fail.append(acc)

        done_acc = ""
        fail_acc = ""

        for acc in done:
            done_acc += acc+" | "

        for acc in fail:
            fail_acc += acc+" | "

        if done_acc != "":
            embed_last.add_field(name="Status", value="""
    *Scrobble de `"""+artist+""" - """+track+"""` feito com êxito!*
    Contas: *| """+done_acc+"""*
    """, inline=False)

        if fail_acc != "":
            embed_last.add_field(name="Aviso", value="""
    *Falha ao scrobblar para: | """+fail_acc+"""*
    """, inline=False)

        return embed_last
