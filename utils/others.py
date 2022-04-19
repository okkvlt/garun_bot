import discord
import requests
import xmltodict
from config.bot import bot
from config.config import API_KEY

from utils.auth import get_signature
from utils.database import get_sk

api = "https://ws.audioscrobbler.com/2.0/"


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

    r = requests.get(api, params=params)

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

    r = requests.post(api, params=data)

    status = xmltodict.parse(r.text)["lfm"]["@status"]
    embed = getEmbed()

    if status != "ok":
        embed.add_field(name="Status", value="""
        *Falha ao realizar esta ação.*
        **Erro:** *"""+xmltodict.parse(r.text)["lfm"]["error"]["#text"]+"""*
        """, inline=False)
        return embed

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


def get_trackImage(artist, track):
    params = {"method": "track.getInfo",
              "api_key": API_KEY,
              "artist": artist,
              "track": track,
              "format": "json"}

    r = requests.get(api, params=params)
    data = r.json()["track"]
    
    if "album" in data:
        return data["album"]["image"][3]["#text"]


def nowPlayingScrobble(id_dict, artist, track, time, mode):
    if not len(id_dict) > 0:
        return

    sucess = "| "
    fail = "| "

    for id in id_dict:
        acc = id_dict[id]

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

        r = requests.post(api, data=data)
        xml = xmltodict.parse(r.text)

        if xml["lfm"]["@status"] != "ok":
            fail += acc + " | "
        else:
            sucess += acc + " | "

    embed = getEmbed()
    embed.set_thumbnail(url=get_trackImage(artist, track))

    if sucess != "| ":
        if mode == 1:
            embed.add_field(name="Status", value="*Scrobbling...!*", inline=False)
        else:
            embed.add_field(name="Status", value="*Scrobbling bem sucedido!*", inline=False)

        embed.add_field(name="Artista", value=artist, inline=False)

        embed.add_field(name="Música", value=track, inline=False)

        embed.add_field(name="Scrobblers", value=sucess, inline=False)

    if fail != "| ":
        embed.add_field(name="Fail", value=fail, inline=False)

    return embed
