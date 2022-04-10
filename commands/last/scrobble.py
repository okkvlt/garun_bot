import re
import sqlite3
import time

import discord
from bot import bot
from commands.last.utils import (check_auth_sessions, get_scrobblers, getEmbed,
                                 scrobbleTrack)
from conf import DB


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
                *Atividade de Scrobbling **ativada!***
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
                *Atividade de Scrobbling **desativada!***
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

                artist = re.search(".+-", description).group(0)[:-2]
                track = re.search("-.+", description).group(0)[2:]

                timestamp = int(time.time())

                scrobblers = get_scrobblers()  # DICT

                if len(scrobblers) > 0:
                    return await message.channel.send(embed=scrobbleTrack(scrobblers, artist, track, timestamp))
        except Exception as error:
            continue
