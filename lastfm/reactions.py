
from config.bot import bot
from utils.auth import check_auth_sessions
from utils.others import get_trackImage, getEmbed, loveTrack


async def reaction(message):
    for embed in message.embeds:
        content = embed.to_dict()
        status = content["fields"][0]["value"]

    if status != "*Scrobbling...!*":
        return

    await message.add_reaction('❤️')
    return await message.add_reaction('🚫')


async def check_reactions(reaction, user, mode):
    if user.id == bot.user.id:
        return

    msg = reaction.message

    if check_auth_sessions(user.id, 1) != 1:
        embed = getEmbed()

        embed.add_field(name="Status",
                        value="É preciso estar autenticado para utilizar essa função.",
                        inline=False)

        return await msg.channel.send(embed=embed,
                                      delete_after=15)

    for embed in msg.embeds:
        fields = embed.to_dict()
        status = fields["fields"][0]["value"]

    if status != "*Scrobbling...!*":
        return

    artist = fields["fields"][1]["value"]
    track = fields["fields"][2]["value"]

    if str(reaction) == '❤️':
        return await msg.channel.send(embed=loveTrack(user.id,
                                                      artist,
                                                      track,
                                                      mode),
                                      delete_after=15)

    if str(reaction) == '🚫':
        embed = getEmbed()

        if get_trackImage(artist,track):
            embed.set_thumbnail(url=get_trackImage(artist,
                                                   track))

        embed.add_field(name="Status",
                        value="*Scrobbling interrompido!*",
                        inline=False)

        embed.add_field(name="Artista", 
                        value=artist, 
                        inline=False)

        embed.add_field(name="Música", 
                        value=track, 
                        inline=False)

        return await msg.edit(embed=embed,
                              delete_after=15)
