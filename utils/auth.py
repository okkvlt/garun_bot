import sqlite3
from hashlib import md5

import requests
from bot import bot
from conf import API_KEY, API_SECRET, DB


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


def check_auth_sessions(id, mode):
    users = get_users()

    count = 0
    check = 0

    for user in users:
        if id == user[0]:
            check = 1
            break
        count += 1

    if mode == 1:
        return check
    else:
        return count


def get_token():
    params = {"method": "auth.gettoken",
              "api_key": API_KEY,
              "format": "json"}

    r = requests.get("https://ws.audioscrobbler.com/2.0/",
                     params=params)

    token = r.json()["token"]

    return token


def get_signature(params):
    sorted_params = sorted(params)

    string = ""

    for param in sorted_params:
        string += param+params[param]

    string += API_SECRET

    sig = md5(string.encode()).hexdigest()

    return sig


def get_session(token, sig):
    params = {"method": "auth.getSession",
              "api_key": API_KEY,
              "token": token,
              "api_sig": sig,
              "format": "json"}

    r = requests.get("https://ws.audioscrobbler.com/2.0/",
                     params=params)

    return r.json()
