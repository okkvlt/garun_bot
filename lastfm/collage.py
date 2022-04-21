import io

import discord
from config.config import COLLAGE
from utils.others import getEmbed


async def collage(message):
    msg = message.content
    data = msg.split()

    periods = ["overall", "7day", "1month", "12month"]

    modes = {
        "albums": COLLAGE.gen_top_albums_collage,
        "artists": COLLAGE.gen_top_artists_collage
    }

    sizes = {
        "3x3": {
            "limit": 9,
            "img_size": 999,
            "art_size": 333
        },

        "4x4": {
            "limit": 16,
            "img_size": 1000,
            "art_size": 250
        },

        "5x5": {
            "limit": 25,
            "img_size": 1000,
            "art_size": 200
        },

        "10x10": {
            "limit": 100,
            "img_size": 2000,
            "art_size": 200
        }
    }

    fail = getEmbed()

    fail.add_field(name="Status",
                   value="*Formato inválido!*",
                   inline=False)

    fail.add_field(name="Syntax:",
                   value="*`$collage [modo] [user] [NxN] [período]`*",
                   inline=False)

    fail.add_field(name="Params:",
                   value="""
                    • **Modo:** *'albums', 'artists'*;
                    • **User:** *last.fm username*;
                    • **NxN:** *'3x3', '4x4', '5x5', '10x10'*;
                    • **Período:** *'7day', '1month', '12month', 'overall'*;
                   """,
                   inline=False)

    if len(data) != 5:
        return await message.channel.send(embed=fail)

    mode = data[1]
    user = data[2]
    size = data[3]
    period = data[4]

    if mode not in modes.keys():
        return await message.channel.send(embed=fail)

    if not size in sizes.keys():
        return await message.channel.send(embed=fail)

    if not period in periods:
        return await message.channel.send(embed=fail)

    await message.channel.send("Gerando colagem...! (Isso pode demorar alguns minutos)")

    try:
        mode_function = modes[mode]
        collage_size = sizes[size]
        img = mode_function(user,
                            period,
                            collage_size["limit"],
                            art_width=collage_size["art_size"],
                            art_height=collage_size["art_size"],
                            collage_width=collage_size["img_size"],
                            collage_height=collage_size["img_size"])

    except Exception as error:
        return await message.channel.send("**Erro ao gerar colagem!**\n**Erro:** *"+str(error)+"*")

    await message.channel.send("Gerando arquivo...!")

    byte = io.BytesIO()

    img.save(byte, 'PNG')
    byte.seek(0)

    return await message.channel.send(file=discord.File(byte, "collage.png"))
