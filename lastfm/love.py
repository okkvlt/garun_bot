import re

from utils.auth import check_auth_sessions
from utils.others import getEmbed, loveTrack


async def love_track(message):
    msg = message.content
    data = msg.split()
    command = data[0]

    modes = {
        "$love": 1,
        "$unlove": 2
    }

    fail = getEmbed()

    fail.add_field(name="Status",
                   value="*Formato inválido!*",
                   inline=False)

    fail.add_field(name="Syntax:",
                   value="""
                   *`$love [artista] - [música]`*
                   *`$unlove [artista] - [música]`*
                   """,
                   inline=False)

    if len(data) < 4 and '-' not in data:
        return await message.channel.send(embed=fail)

    music = msg.replace(data[0], "")[1:]

    artist = re.search(".+-", music).group(0)[:-2]
    track = re.search("-.+", music).group(0)[2:]

    author_id = message.author.id

    if check_auth_sessions(author_id, 1) != 1:
        auth = getEmbed()

        auth.add_field(name="Status",
                       value="É preciso estar autenticado para utilizar essa função.",
                       inline=False)

        return await message.channel.send(embed=auth,
                                          delete_after=15)

    try:
        return await message.channel.send(embed=loveTrack(author_id,
                                                          artist,
                                                          track,
                                                          modes[command]),
                                          delete_after=15)
    except Exception as error:
        fail = getEmbed()
        fail.add_field(name="Status — Erro",
                       value="**Erro:** *"+str(error)+"*",
                       inline=False)
        return await message.channel.send(embed=fail)
