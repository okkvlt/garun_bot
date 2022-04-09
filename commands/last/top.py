import discord
from bot import bot
from commands.last.utils import get_topAlbums, get_topArtists, getEmbed

async def top(message, id):
    data = message.content.split()

    embed_last = getEmbed()

    if len(data) != 4:
        embed_last.add_field(name="Status", value="""
*Formato inválido!*
""", inline=False)

        if id == 1:
            embed_last.add_field(name="Utilize:", value="""
`$top_albums (user) (n) (overall/7days/1month/12month)`
    """, inline=False)
        else:
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

    if id == 1:
        r = get_topAlbums(user, n, time)
    else:
        r = get_topArtists(user, n, time)

    if not "error" in r:
        if id == 1:
            top = r["topalbums"]["album"]

            embed_last.set_author(name="Garun — Top "+n+" albums",
                                  icon_url='https://i.imgur.com/59qD9SY.jpg')

        else:
            top = r["topartists"]["artist"]

            embed_last.set_author(name="Garun — Top "+n+" artistas",
                                  icon_url='https://i.imgur.com/59qD9SY.jpg')

        value = ""

        if id == 1:
            for album in top:
                value += "**"+album["@attr"]["rank"]+"º**: *"+album["artist"]["name"]+" — " + \
                    album["name"]+" ("+album["playcount"]+" plays).*\n"
        else:
            for artist in top:
                value += "**"+artist["@attr"]["rank"]+"º** — *" + \
                    artist["name"]+" ("+artist["playcount"]+" plays).*\n"

        embed_last.add_field(
            name="Usuário: ", value="`"+user+"`", inline=False)

        if id == 1:
            embed_last.add_field(name="Top "+str(n) +
                                 " albums", value=value, inline=False)
        else:
            embed_last.add_field(name="Top "+str(n) +
                                 " artistas", value=value, inline=False)

        return await message.channel.send(embed=embed_last)

    embed_last.add_field(name="Status", value="Erro: " +
                         str(r["error"])+"\nMensagem: `"+r["message"]+"`", inline=False)

    return await message.channel.send(embed=embed_last)
