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
