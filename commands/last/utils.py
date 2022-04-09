import discord
import requests
from hashlib import md5
from bot import bot
from conf import API_KEY, API_SECRET


def get_token():
    r = requests.get(
        "https://ws.audioscrobbler.com/2.0/?method=auth.gettoken&api_key="+API_KEY+"&format=json")

    return r.json()["token"]

def get_signature(token):
    sig = md5(("api_key"+API_KEY+"methodauth.getSessiontoken" +
              token+API_SECRET).encode()).hexdigest()
    
    return sig

def get_session(token):
    sig = get_signature(token)

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


def scrobbleTrack(message):
    arq = open(".session", "r")
    for auth in arq:
        auth = auth.split()
        if auth[0] == message.author.id:
            did = auth[0]
            user = auth[1]
            sk = auth[2]
            sig = auth[3]
    
    arq.close()
    
    if not did:
        return "Usuário `"+user+"` não autenticado!"

    #r = requests.post("http://ws.audioscrobbler.com/2.0/", )
    #continue


def getEmbed():
    embed = discord.Embed(colour=0xedd58d)

    embed.set_author(name="Garun — Last.fm",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    embed.set_footer(
        text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')
    
    return embed