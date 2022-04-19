import discord
from config.bot import bot

from lastfm.auth import auth, disconnect, session
from lastfm.help import help_message
from lastfm.love import love_track
from lastfm.scrobble import hydra, scrobble, tempo
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
        return await scrobble(message)

    if message.content == "$disconnect":
        return await disconnect(message)

    if message.author.name == "Hydra":
        return await hydra(message)

    if message.content == "$help":
        return await help_message(message)

    if "$love" in message.content:
        return await love_track(message, 1)

    if "$unlove" in message.content:
        return await love_track(message, 2)

    if message.author.name == "Tempo":
        return await tempo(message)
