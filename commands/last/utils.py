from hashlib import md5
import sqlite3

from sympy import EX

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
        print(error)

    c.commit()
    c.close()

    return 1


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


def scrobbleTrack(message, artist, track, time):
    c = sqlite3.connect(DB)
    ex = c.cursor()

    try:
        rows = ex.execute("SELECT * FROM users")
        users = rows.fetchall()
    except Exception as error:
        return str(error)

    count = 0

    for user in users:
        if message.author.id == user[0]:
            check = 1
            break
        count += 1

    if check == 0:
        return "Você não está autenticado!"

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
        embed_last.add_field(name="Sucesso", value="""
*Scrobble de `"""+artist+""" - """+track+"""` feito com êxito!*
""", inline=False)

        return embed_last

    embed_last.add_field(name="Erro", value="""
*Falha no scrobble de `"""+artist+""" - """+track+"""`.*
""", inline=False)

    return embed_last
