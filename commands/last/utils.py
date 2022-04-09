import discord
import requests
from hashlib import md5
from bot import bot
from conf import API_KEY, API_SECRET


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
    arq = open(".sessions", "r")

    check = 0

    for auth in arq:
        auth = auth.split()
        if auth[0] == str(message.author.id):
            check = 1

    arq.close()

    if check == 0:
        return "Você não está autenticado!"

    sk = auth[2]

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

    if 'accepted="1"' in r.text:
        embed_last.add_field(name="Sucesso", value="""
*Scrobble de `"""+artist+""" - """+track+"""` feito com êxito!*
""", inline=False)
        
        return embed_last
    
    embed_last.add_field(name="Erro", value="""
*Falha no scrobble de `"""+artist+""" - """+track+"""`.*
""", inline=False)
    
    return embed_last