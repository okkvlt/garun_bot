import discord
from bot import bot
from conf import DB
from utils.auth import get_users


@bot.event
async def on_ready():
    print(f'{bot.user} is online!')

    if len(bot.guilds) != 0:
        print(f'\n{bot.user} está em '+str(len(bot.guilds))+' guildas:\n')

        print("[guild.id - guild.name]")
        for guild in bot.guilds:
            print(f"{guild.id} - {guild.name}")

    else:
        print("Nenhuma guilda!")

    if len(get_users()) != 0:
        print("\n"+str(len(get_users()))+" sessões iniciadas:\n")

        print("[user.id, last.fm acc, session_key, scrobbling]")
        for user in get_users():
            print(user)

    else:
        print("Nenhuma sessão!")
