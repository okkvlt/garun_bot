import discord
from bot import bot
from commands.last.utils import get_token
from conf import API_KEY


@bot.event
async def on_message(message):
    if message.content == "$connect":
        embed_last = discord.Embed(colour=0xedd58d)

        embed_last.set_author(name="Garun — Last.fm",
                              icon_url='https://i.imgur.com/59qD9SY.jpg')

        embed_last.set_footer(
            text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

        if not isinstance(message.channel, discord.channel.DMChannel):
            embed_last.add_field(name="Status", value="""
Informações enviadas via privado...
""", inline=False)

            await message.channel.send(embed=embed_last)

        embed_last.clear_fields()

        embed_last.add_field(name="Tutorial", value="""
`$connect (username) (password)` — *conecta-se com a conta informada.*
""", inline=False)

        return await message.author.send(embed=embed_last)

    if "$connect " in message.content:
        embed_last = discord.Embed(colour=0xedd58d)

        embed_last.set_author(name="Garun — Last.fm",
                              icon_url='https://i.imgur.com/59qD9SY.jpg')

        embed_last.set_footer(
            text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

        if not isinstance(message.channel, discord.channel.DMChannel):
            embed_last.add_field(name="Status", value="""
Utilize comunicação privada para enviar informações da conta!
Informações enviadas via privado...
""", inline=False)

            await message.channel.send(embed=embed_last)

            embed_last.clear_fields()

            embed_last.add_field(name="Tutorial", value="""
`$connect (username) (password)` — *conecta-se com a conta informada.*
""", inline=False)

            return await message.author.send(embed=embed_last)

        data = message.content.split()

        if len(data) != 3:

            embed_last.add_field(name="Tutorial", value="""
`$connect (username) (password)` — *conecta-se com a conta informada.*
""", inline=False)

            return await message.author.send(embed=embed_last)

        user = data[1]
        password = data[2]

        embed_last.add_field(name="Status", value="""
Usuário — `"""+user+"""`
Senha — `"""+password+"""`
""", inline=False)

        token = get_token()

        embed_last.add_field(name="Autorize o BOT", value="""
*[http://www.last.fm/api/auth/?api_key="""+API_KEY+"""&token="""+token+"""]*
""", inline=False)

        embed_last.add_field(name="Tutorial", value="""
**1º** - *Clique no link acima.*
**2º** - *Autorize o acesso do BOT à sua conta.*

**Após isso, o BOT estará conectado!**
""", inline=False)

        await message.author.send(embed=embed_last)
