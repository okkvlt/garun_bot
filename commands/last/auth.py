import sqlite3
from string import hexdigits

import discord
from bot import bot
from commands.last.utils import get_session, get_signature, get_token, getEmbed, insert_session
from conf import API_KEY, API_SECRET


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
**Ex.: ** *$session bCXd57FOYxy5Z6cTxla5GIDlc0UejQlO*""")

        return await message.author.send(embed=embed_last)

    token = data[1]

    params = {"api_key": API_KEY,
              "method": "auth.getSession",
              "token": token}

    sig = get_signature(params)
    r = get_session(token, sig)

    if not "error" in r:
        embed_last.add_field(
            name="Status", value="Vínculo realizado com sucesso!")

        s = r["session"]
        
        id = message.author.id
        last_user = s["name"]
        session_key = s["key"]

        insert_session(id, last_user, session_key)
        
        return await message.author.send(embed=embed_last)

    embed_last.add_field(name="Status", value="**Erro:** " +
                         str(r["error"])+" — *`"+r["message"]+"`.*")

    return await message.author.send(embed=embed_last)
