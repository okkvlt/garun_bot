import re
import sqlite3
import time

import discord
from bot import bot
from commands.last.utils import getEmbed, check_auth_sessions
from conf import DB


async def love_track(message, mode):
    data = message.content.split()
    embed = getEmbed
    
    c = sqlite3.connect(DB)
    ex = c.cursor()
    
    if data != 2:
        embed.add_field(name="Status — Erro", value="""
        *É necessário informar (apenas) o id da música>
        **Exemplo: ** *`$love [music_id]`* ou *`$unlove [music_id]`*
        """)
        return await message.channel.send(embed=embed)
    
    music_id = data[1]
    author_id = message.author.id
    
    """if check_auth_sessions(author_id, 1) == 1:
        try:
            
        except:"""
            