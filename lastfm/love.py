import re

from utils.auth import check_auth_sessions
from utils.others import getEmbed, loveTrack


async def love_track(message, mode):
    data = message.content.split()
    embed = getEmbed()

    if len(data) == 1:
        embed.add_field(name="Status — Erro", value="""
        *É necessário informar a música!*
        **Exemplo: ** *`$love "artist - track"`* ou *`$unlove "artist - track"`*
        """, inline=False)
        return await message.channel.send(embed=embed)

    temp = data[1:]
    music = ""

    for x in temp:
        music += x+" "

    artist = re.search(".+-", music).group(0)[:-2]
    track = re.search("-.+", music).group(0)[2:-1]

    author_id = message.author.id

    if check_auth_sessions(author_id, 1) == 1:
        try:
            return await message.channel.send(embed=loveTrack(author_id, artist, track, mode))
        except Exception as error:
            embed.add_field(name="Status — Erro", value="""
            **Erro:** *"""+str(error)+"""*
            """, inline=False)
            return await message.channel.send(embed=embed)
