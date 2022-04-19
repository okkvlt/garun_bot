from config.bot import bot
from config.config import HYDRA, TEMPO

from lastfm.auth import auth, disconnect, session
from lastfm.help import help_message
from lastfm.love import love_track
from lastfm.reactions import check_reactions, reaction
from lastfm.scrobble import hydra, scrobble_after_delete, scrobble_on_off, tempo
from lastfm.top import top


@bot.event
async def on_message(message):
    if "$top_artists" in message.content:
        return await top(message, 2)

    if "$top_albums" in message.content:
        return await top(message, 1)

    if message.content == "$connect":
        return await auth(message)

    if "$session" in message.content:
        return await session(message)

    if "$scrobble" in message.content:
        return await scrobble_on_off(message)

    if message.content == "$disconnect":
        return await disconnect(message)

    if message.author.id == HYDRA:
        return await hydra(message)

    if message.content == "$help":
        return await help_message(message)

    if "$love" in message.content:
        return await love_track(message, 1)

    if "$unlove" in message.content:
        return await love_track(message, 2)

    if message.author.id == TEMPO:
        return await tempo(message)

    if message.author.id == bot.user.id:
        return await reaction(message)


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author.id == bot.user.id:
        return await check_reactions(reaction, user, 1)


@bot.event
async def on_reaction_remove(reaction, user):
    if reaction.message.author.id == bot.user.id:
        return await check_reactions(reaction, user, 2)


@bot.event
async def on_message_delete(message):
    if message.author.id == bot.user.id:
        return await scrobble_after_delete(message)
