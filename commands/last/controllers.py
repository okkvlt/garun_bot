import discord
from bot import bot
from commands.last.top import top
from commands.last.auth import auth

@bot.event
async def on_message(message):
    if "$top_artists" in message.content:
        return await top(message, 2)

    if "$top_albums" in message.content:
        return await top(message, 1)

    if "$connect" in message.content:
        return await auth(message)