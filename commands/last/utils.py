import discord
import requests
from hashlib import md5
from bot import bot
from conf import API_KEY, API_SECRET


def get_token():
    r = requests.get(
        "https://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key="+API_KEY+"&format=json")

    return r.json()["token"]


def get_session(token):
    sig = md5(("api_key"+API_KEY+"methodauth.getSessiontoken" +
              token+API_SECRET).encode()).hexdigest()

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


# def scrobbleTrack():
    # print(get_session("D7Q7QxoZXsfTmBxQZz8JGfWbIm1mojvR"))


def getEmbed():
    embed = discord.Embed(colour=0xedd58d)

    embed.set_author(name="Garun — Last.fm",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    embed.set_footer(
        text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')
    
    return embed