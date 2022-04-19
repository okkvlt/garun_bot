
from config.bot import bot
from utils.others import get_trackImage, getEmbed, loveTrack


async def reaction(message):
    for embed in message.embeds:
        content = embed.to_dict()
        status = content["fields"][0]["value"]

        if status == "*Scrobbling...!*":
            await message.add_reaction('❤️')
            return await message.add_reaction('🚫')


async def check_reactions(reaction, user, mode):
    if user.id != bot.user.id:
        cont = reaction.message
        for embed in cont.embeds:
            content = embed.to_dict()
            status = content["fields"][0]["value"]

            if status == "*Scrobbling...!*":
                artist = content["fields"][1]["value"]
                track = content["fields"][2]["value"]
                if str(reaction) == '❤️':
                    return await cont.channel.send(embed=loveTrack(user.id, artist, track, mode))
                if str(reaction) == '🚫':
                    embed = getEmbed()

                    embed.set_thumbnail(url=get_trackImage(artist, track))

                    embed.add_field(name="Status", value="""
                    *Scrobbling interrompido!*
                    """, inline=False)

                    embed.add_field(name="Artista", value=artist, inline=False)

                    embed.add_field(name="Música", value=track, inline=False)

                    return await cont.edit(embed=embed, delete_after=15)
