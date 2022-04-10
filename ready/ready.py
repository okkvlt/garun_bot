import discord
from bot import bot
from conf import DB
from commands.last.utils import get_users


@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

    if len(bot.guilds) != 0:
        print(f'\n{bot.user} is in '+str(len(bot.guilds))+' guild(s):')

        for guild in bot.guilds:
            print(f"{guild.id} - {guild.name}")

    if len(get_users()) != 0:
        print("\n"+str(len(get_users()))+" sessões iniciadas:")

        for user in get_users():
            print(user)
