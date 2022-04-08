import discord
import pylast
from bot import bot
from conf import API_KEY, API_SECRET, LAST_USER, LAST_PASS


@bot.event
async def on_message(message):
    if message.content == "$connect":
        embed_last = discord.Embed(colour=0xedd58d)

        embed_last.set_author(name="Garun — Last.fm",
                              icon_url='https://i.imgur.com/59qD9SY.jpg')

        embed_last.set_footer(text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

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
