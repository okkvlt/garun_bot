import re
import sqlite3
import time

from config.config import DB
from utils.auth import check_auth_sessions
from utils.database import get_scrobblers
from utils.others import getEmbed, nowPlayingScrobble


async def scrobble_on_off(message):
    data = message.content.split()
    embed = getEmbed()

    c = sqlite3.connect(DB)
    ex = c.cursor()

    if len(data) != 2:
        embed.add_field(name="Status — Erro", value="""
        *É necessário informar (apenas) se o scrobbling será ativado (on) ou desativado (off)>
        **Exemplo: ** *`$scrobble on`* ou *`$scrobble off`.*
        """)

        return await message.channel.send(embed=embed,
                                          delete_after=30)

    if check_auth_sessions(message.author.id, 1) != 1:
        embed.add_field(name="Status — Erro", value="""
        *Você **precisa** estar autenticado ao BOT!*
        **Conecte-se:** *`$connect`*
        """)

        return await message.channel.send(embed=embed,
                                          delete_after=30)

    if data[1] == "on":
        try:
            ex.execute("UPDATE users SET scrobbling = 1 WHERE id = " +
                       str(message.author.id))
            embed.add_field(name="Status",
                            value="*Scrobbling **ativado!***")
            c.commit()
            c.close()

        except Exception as error:
            embed.add_field(name="Erro", value="""
            *Erro ao ativar scrobbling.*
            **Erro:** *`"""+str(error)+"""`.*
            """)

    elif data[1] == "off":
        try:
            ex.execute("UPDATE users SET scrobbling = 0 WHERE id = " +
                       str(message.author.id))
            embed.add_field(name="Status",
                            value="*Scrobbling **desativado!***")
            c.commit()
            c.close()

        except Exception as error:
            embed.add_field(name="Erro", value="""
            *Erro ao desativar scrobbling.*
            **Erro:** *`"""+str(error)+"""`.*
            """)

    else:
        embed.add_field(name="Status — Erro", value="""
        *Argumento """+str(data[1])+""" **inválido!***
        *É necessário informar (apenas) se o scrobbling será ativado (on) ou desativado (off)*
        **Exemplo: ** *`$scrobble on`* ou *`$scrobble off`.*
        """)

    return await message.channel.send(embed=embed,
                                      delete_after=30)


async def hydra(message):
    if not message.embeds:
        return

    for embed in message.embeds:
        msg = embed.to_dict()

    if not "title" in msg:
        return

    title = msg["title"]

    if title != "Now playing":
        return

    description = msg["description"]

    track = re.search("-.+", description).group(0)[2:]
    artist = description.replace(track, "")[:-3]

    timestamp = int(time.time())

    members = message.author.voice.channel.members

    scrobblers = get_scrobblers(members, 1)

    if not scrobblers:
        return

    return await message.channel.send(embed=nowPlayingScrobble(scrobblers,
                                                               artist,
                                                               track,
                                                               timestamp,
                                                               1),
                                      delete_after=60)


async def tempo(message):
    if not message.embeds:
        return

    for embed in message.embeds:
        msg = embed.to_dict()

    if not "author" in msg:
        return

    title = msg["author"]["name"]

    if not "Playing: " in title:
        return

    track = re.search("-.+", title).group(0)[2:]
    artist = title.replace(track, "")[9:-3]

    timestamp = int(time.time())

    members = message.author.voice.channel.members

    scrobblers = get_scrobblers(members, 1)

    if not scrobblers:
        return

    return await message.channel.send(embed=nowPlayingScrobble(scrobblers,
                                                               artist,
                                                               track,
                                                               timestamp,
                                                               1),
                                      delete_after=60)


async def scrobble_after_delete(message):
    if not message.embeds:
        return

    for embed in message.embeds:
        msg = embed.to_dict()

    status = msg["fields"][0]["value"]

    if status != "*Scrobbling...!*":
        return

    members = []

    artist = msg["fields"][1]["value"]
    track = msg["fields"][2]["value"]
    listeners = msg["fields"][3]["value"].split()

    timestamp = int(time.time())

    for m in listeners:
        if m != '|':
            members.append(m)

    scrobblers = get_scrobblers(members, 2)

    if not scrobblers:
        return

    return await message.channel.send(embed=nowPlayingScrobble(scrobblers,
                                                               artist,
                                                               track,
                                                               timestamp,
                                                               2),
                                      delete_after=60)
