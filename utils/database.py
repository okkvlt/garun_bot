import sqlite3
from hashlib import md5

from bot import bot
from conf import DB

from utils.auth import check_auth_sessions


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


def get_sk(id):
    c = sqlite3.connect(DB)
    ex = c.cursor()

    count = check_auth_sessions(id, 2)

    try:
        rows = ex.execute("SELECT * FROM users")
        users = rows.fetchall()
    except Exception as error:
        return str(error)

    sk = users[count][2]

    return sk


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
