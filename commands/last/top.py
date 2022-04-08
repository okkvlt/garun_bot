import discord
from bot import bot
from commands.last.utils import top


@bot.event
async def on_message(message):
    if "$top_artists" in message.content:
        return await top(message, 2)

    if "$top_albums" in message.content: #1
        return await top(message, 1)