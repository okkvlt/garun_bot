from string import hexdigits
import discord
from bot import bot
from commands.last.utils import get_token, get_session, getEmbed
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
        return print("a")
    
    token = data[1]
    r = get_session(token)
    
    if not "error" in r:
        embed_last.add_field(name="Status", value="Vínculo realizado com sucesso!")
        
        s = r["session"]
        
        arq = open(".sessions", "a")
        arq.write(str(message.author.id)+" "+s["name"]+" "+s["key"]+"\n")
        arq.close()
        
        return await message.author.send(embed=embed_last)
    
    embed_last.add_field(name="Status", value="**Erro:** "+str(r["error"])+" — *`"+r["message"]+"`.*")
    
    return await message.author.send(embed=embed_last)