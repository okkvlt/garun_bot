import re
import sqlite3
import time

from config.config import DB
from utils.auth import check_auth_sessions
from utils.database import get_scrobblers
from utils.others import getEmbed, nowPlaying_and_Scrobble


async def scrobble(message):
    data = message.content.split()
    embed = getEmbed()

    c = sqlite3.connect(DB)
    ex = c.cursor()

    if len(data) != 2:
        embed.add_field(name="Status — Erro", value="""
        *É necessário informar (apenas) se o scrobbling será ativado (on) ou desativado (off)>
        **Exemplo: ** *`$scrobble on`* ou *`$scrobble off`.*
        """)
        return await message.channel.send(embed=embed)

    if data[1] == "on":
        try:
            if check_auth_sessions(message.author.id, 1) == 1:

                ex.execute(
                    "UPDATE users SET scrobbling = 1 WHERE id = "+str(message.author.id))
                embed.add_field(name="Status", value="""
                *Scrobbling **ativado!***
                """)
                c.commit()
                c.close()

            else:
                embed.add_field(name="Status — Erro", value="""
                *Você **precisa** estar autenticado ao BOT!*
                **Conecte-se:** *`$connect`*
                """)

        except Exception as error:
            embed.add_field(name="Erro", value="""
            *Erro ao ativar scrobbling.*
            **Erro:** *`"""+str(error)+"""`.*
            """)

    elif data[1] == "off":
        try:
            if check_auth_sessions(message.author.id, 1) == 1:

                ex.execute(
                    "UPDATE users SET scrobbling = 0 WHERE id = "+str(message.author.id))
                embed.add_field(name="Status", value="""
                *Scrobbling **desativado!***
                """)
                c.commit()
                c.close()

            else:
                embed.add_field(name="Status — Erro", value="""
                *Você **precisa** estar autenticado ao BOT!*
                **Conecte-se:** *`$connect`*
                """)

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

    return await message.channel.send(embed=embed)


async def hydra(message):
    for embed in message.embeds:
        content = embed.to_dict()

        try:
            title = content["title"]

            if title == "Now playing":
                description = content["description"]

                track = re.search("-.+", description).group(0)[2:]
                artist = description.replace(track, "")[:-3]

                timestamp = int(time.time())

                scrobblers = get_scrobblers()

                if len(scrobblers) > 0:
                    return await message.channel.send(embed=nowPlaying_and_Scrobble(scrobblers, artist, track, timestamp, 1),
                                                      delete_after=60)
        except Exception as error:
            continue


async def tempo(message):
    for embed in message.embeds:
        content = embed.to_dict()

        try:
            title = content["author"]["name"]

            if "Playing: " in title:

                track = re.search("-.+", title).group(0)[2:]
                artist = title.replace(track, "")[9:-3]

                timestamp = int(time.time())

                scrobblers = get_scrobblers()

                if len(scrobblers) > 0:
                    return await message.channel.send(embed=nowPlaying_and_Scrobble(scrobblers, artist, track, timestamp, 1),
                                                      delete_after=60)
        except Exception as error:
            continue


async def scrobble_track(message):
    for embed in message.embeds:
        content = embed.to_dict()
        status = content["fields"][0]["value"]

        if status == "*Scrobbling...!*":
            artist = content["fields"][1]["value"]
            track = content["fields"][2]["value"]

            timestamp = int(time.time())

            scrobblers = get_scrobblers()

            if len(scrobblers) > 0:
                return await message.channel.send(embed=nowPlaying_and_Scrobble(scrobblers, artist, track, timestamp, 2),
                                                  delete_after=60)
