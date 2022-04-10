import discord
from bot import bot
from commands.last.auth import auth, disconnect, session
from commands.last.scrobble import hydra, scrobble
from commands.last.top import top


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
