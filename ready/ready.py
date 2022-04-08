import discord
from bot import bot


@bot.event
async def on_ready():
    print(f'{bot.user} is online!\n')

    if len(bot.guilds) != 0:
        print(f'{bot.user} is in '+str(len(bot.guilds))+' guild(s):\n')

        for guild in bot.guilds:
            print(f"{guild.id} - {guild.name}")
