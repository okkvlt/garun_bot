import discord
from bot import bot
from commands.last.utils import get_topArtists


@bot.event
async def on_message(message):
    if "$top_artists" in message.content:
        data = message.content.split()

        embed_last = discord.Embed(colour=0xedd58d)

        embed_last.set_author(name="Garun — Top artistas",
                              icon_url='https://i.imgur.com/59qD9SY.jpg')

        embed_last.set_footer(
            text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

        if len(data) != 4:
            embed_last.add_field(name="Status", value="""
*Formato inválido!*
""", inline=False)

            embed_last.add_field(name="Utilize:", value="""
`$top_artists (user) (n) (overall/7days/1month/12month)`
""", inline=False)

            embed_last.add_field(name="Parâmetros:", value="""
**user:** *usuário.*
**n:** *top (n).*
**(overall/7day/1month/12month):** *período de tempo.*
""", inline=False)

            return await message.channel.send(embed=embed_last)

        user = data[1]
        n = data[2]
        time = data[3]

        r = get_topArtists(user, n, time)

        if not "error" in r:
            top = r["topartists"]["artist"]

            embed_last.set_author(name="Garun — Top "+n+" artistas",
                                  icon_url='https://i.imgur.com/59qD9SY.jpg')

            value = ""
            for artist in top:
                value += "**"+artist["@attr"]["rank"]+"º** — *" + \
                    artist["name"]+" ("+artist["playcount"]+" plays).*\n"

            embed_last.add_field(
                name="Usuário: ", value="`"+user+"`", inline=False)

            embed_last.add_field(name="Top "+str(n) +
                                 " artistas", value=value, inline=False)

            return await message.channel.send(embed=embed_last)

        embed_last.add_field(name="Status", value="Erro: " +
                             str(r["error"])+"\nMensagem: `"+r["message"]+"`", inline=False)

        return await message.channel.send(embed=embed_last)
