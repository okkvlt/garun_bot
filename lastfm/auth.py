import sqlite3
from string import hexdigits

import discord
from bot import bot
from conf import API_KEY, API_SECRET, DB
from utils.auth import (check_auth_sessions, get_session, get_signature,
                        get_token)
from utils.database import insert_session
from utils.others import getEmbed


async def auth(message):
    embed_last = getEmbed()

    if not isinstance(message.channel, discord.channel.DMChannel):
        embed_last.add_field(name="Status", value="""
        Utilize comunicação privada para enviar informações da conta!
        Informações enviadas via privado...
        """, inline=False)

        await message.channel.send(embed=embed_last)

    embed_last.clear_fields()
    token = get_token()

    embed_last.add_field(name="**Vincule a conta**", value="""
    *[http://www.last.fm/api/auth/?api_key="""+API_KEY+"""&token="""+token+"""]*

    **1º** - *Clique no link acima.*
    **2º** - *Autorize o acesso do BOT à sua conta.*
    """, inline=False)

    embed_last.add_field(name="**Ative a sessão**", value="""
    **Digite:** $session `"""+token+"""`

    **Após isso, o BOT estará vinculado!**
    """, inline=False)

    return await message.author.send(embed=embed_last)


async def session(message):
    embed_last = getEmbed()

    data = message.content.split()

    if len(data) != 2:
        embed_last.add_field(name="Status", value="""
        **Erro:** """ + """*é necessário informar (apenas) o token.*
        **Ex.: ** *$session bCXd57FOYxy5Z6cTxla5GIDlc0UejQlO*
        """)

        return await message.author.send(embed=embed_last)

    token = data[1]

    params = {"api_key": API_KEY,
              "method": "auth.getSession",
              "token": token}

    sig = get_signature(params)
    r = get_session(token, sig)

    if not "error" in r:
        embed_last.add_field(
            name="Status", value="*Vínculo realizado com sucesso!*")

        s = r["session"]

        id = message.author.id
        last_user = s["name"]
        session_key = s["key"]

        if insert_session(id, last_user, session_key) != 1:
            embed_last.add_field(name="Banco de Dados", value="""
            ***Erro** ao salvar sessão no banco de dados!*
            **Erro: ** *`"""+str(insert_session(id, last_user, session_key))+"""`*""", inline=False)
            return await message.author.send(embed=embed_last)

        embed_last.add_field(
            name="Banco de Dados", value="*Sessão salva com êxito no banco de dados!*", inline=False)
        return await message.author.send(embed=embed_last)

    embed_last.add_field(name="Status", value="**Erro:** " +
                         str(r["error"])+" — *`"+r["message"]+"`.*")

    return await message.author.send(embed=embed_last)


async def disconnect(message):
    embed = getEmbed()

    if check_auth_sessions(message.author.id, 1) != 1:
        embed.add_field(name="Status — Erro", value="""
        **Erro:** *é preciso estar autenticado para se desconectar!*
        """, inline=False)

        if not isinstance(message.channel, discord.channel.DMChannel):
            return await message.channel.send(embed=embed)
        return await message.author.send(embed=embed)

    c = sqlite3.connect(DB)
    ex = c.cursor()

    try:
        ex.execute("DELETE FROM users WHERE id = "+str(message.author.id))

        c.commit()
        c.close()

        embed.add_field(name="Status", value="""
        *Sua conta foi desvinculada com sucesso!*
        """, inline=False)

        if not isinstance(message.channel, discord.channel.DMChannel):
            return await message.channel.send(embed=embed)
        return await message.author.send(embed=embed)

    except Exception as error:
        embed.add_field(name="Status — Erro", value="""
        **Erro:** *`"""+str(error)+"""`*
        """, inline=False)

        if not isinstance(message.channel, discord.channel.DMChannel):
            return await message.channel.send(embed=embed)
        return await message.author.send(embed=embed)
