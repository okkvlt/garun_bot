import discord
from bot import bot
from commands.last.top import top
from commands.last.auth import auth, session
from commands.last.scrobble import scrobble

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