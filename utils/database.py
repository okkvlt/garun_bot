import sqlite3

from config.config import DB, TEMPO, HYDRA

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


def get_scrobblers(members, mode):
    c = sqlite3.connect(DB)
    ex = c.cursor()

    id = []
    data = []
    scrobblers = {}

    if mode != 1:
        for acc in members:
            for row in ex.execute("SELECT * FROM users WHERE last_user = '"+acc+"'"):
                id.append(row[0])
    else:
        for m in members:
            if m.id != TEMPO and m.id != HYDRA:
                id.append(m.id)

    if not id:
        return

    for m in id:
        for row in ex.execute("SELECT * FROM users WHERE scrobbling = 1 AND id = "+str(m)):
            data.append(row)

    if not data:
        return

    for scrobbler in data:
        scrobblers[scrobbler[0]] = scrobbler[1]

    c.commit()
    c.close()

    return scrobblers