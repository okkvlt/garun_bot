import discord
import requests
import xmltodict
from config.bot import bot
from config.config import API_KEY

from utils.auth import get_signature
from utils.database import get_sk


def get_top(user, n, time, mode):
    params = {"api_key": API_KEY,
              "user": user,
              "limit": n,
              "period": time,
              "format": "json"}

    if mode == 1:
        params["method"] = "user.gettopartists"
    else:
        params["method"] = "user.gettopalbums"

    r = requests.get("https://ws.audioscrobbler.com/2.0/",
                     params=params)

    return r.json()


def getEmbed():
    embed = discord.Embed(colour=0xedd58d)

    embed.set_author(name="Garun — Last.fm",
                     icon_url='https://i.imgur.com/59qD9SY.jpg')

    embed.set_footer(text=f"Powered by {bot.user}",
                     icon_url='https://i.imgur.com/59qD9SY.jpg')

    return embed


def loveTrack(id, artist, track, mode):
    sk = get_sk(id)

    data = {"artist": artist,
            "track": track,
            "api_key": API_KEY,
            "sk": sk}

    if mode == 1:
        data["method"] = "track.love"
    else:
        data["method"] = "track.unlove"

    sig = get_signature(data)

    data["api_sig"] = sig

    r = requests.post("https://ws.audioscrobbler.com/2.0/",
                      params=data)

    status = xmltodict.parse(r.text)["lfm"]["@status"]
    embed = getEmbed()

    if status == "ok":
        embed.set_thumbnail(url=get_trackImage(artist, track))

        if mode == 1:
            embed.add_field(name="Status", value="""
            *Você amou **'"""+track+"""'** de **'"""+artist+"""'** com sucesso!*
            """, inline=False)
        else:
            embed.add_field(name="Status", value="""
            *Você retirou seu 'amei' de **'"""+track+"""'** de **'"""+artist+"""'** com sucesso!*
            """, inline=False)

        return embed

    embed.add_field(name="Status", value="""
    *Falha ao realizar esta ação.*
    **Erro:** *"""+xmltodict.parse(r.text)["lfm"]["error"]["#text"]+"""*
    """, inline=False)
    return embed


def get_trackImage(artist, track):
    params = {"method": "track.getInfo",
              "api_key": API_KEY,
              "artist": artist,
              "track": track,
              "format": "json"}

    r = requests.get("https://ws.audioscrobbler.com/2.0/", params=params)
    data = r.json()

    return data["track"]["album"]["image"][3]["#text"]


def nowPlaying_and_Scrobble(id_dict, artist, track, time, mode):
    if len(id_dict) > 0:
        done = []
        fail = []

        for session in id_dict:
            id = session
            acc = id_dict[session]

            sk = get_sk(id)

            if mode == 1:
                data = {"artist": artist,
                        "track": track,
                        "method": "track.updateNowPlaying",
                        "duration": "60",
                        "api_key": API_KEY,
                        "sk": sk}

                sig = get_signature(data)

            else:
                data = {"artist": artist,
                        "track": track,
                        "method": "track.scrobble",
                        "timestamp": str(time),
                        "api_key": API_KEY,
                        "sk": sk}

                sig = get_signature(data)
                data["timestamp"] = time

            data["api_sig"] = sig

            r = requests.post("http://ws.audioscrobbler.com/2.0/", data=data)
            print(r.text)

            embed_last = getEmbed()

            if 'status="ok"' in r.text:
                done.append(acc)
            else:
                fail.append(acc)

        done_acc = "| "
        fail_acc = "| "

        for acc in done:
            done_acc += "*"+acc+"* | "

        for acc in fail:
            fail_acc += "*"+acc+"* | "

        if done_acc != "| ":
            embed_last.set_thumbnail(url=get_trackImage(artist, track))

            if mode == 1:
                embed_last.add_field(name="Status", value="""
                *Scrobbling...!*
                """, inline=False)
            else:
                embed_last.add_field(name="Status", value="""
                *Scrobbling bem sucedido!*
                """, inline=False)

            embed_last.add_field(name="Artista", value=artist, inline=False)

            embed_last.add_field(name="Música", value=track, inline=False)

            embed_last.add_field(
                name="Scrobblers", value=done_acc, inline=False)

        if fail_acc != "| ":
            embed_last.add_field(name="Aviso", value="""
            *Falha ao scrobblar para: | """+fail_acc+"""*
            """, inline=False)

        return embed_last
