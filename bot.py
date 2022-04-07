import discord
from decouple import config

TOKEN = config('BOT_TOKEN')

bot = discord.Client()


@bot.event
async def on_ready():
    print(
        f'{bot.user} is online!\n'
    )

    if len(bot.guilds) != 0:
        print(f'{bot.user} is in '+str(len(bot.guilds))+' guild(s):\n')

        for guild in bot.guilds:
            print(f"{guild.id} - {guild.name}")


@bot.event
async def on_message(message):
    if message.content == "/help":
        await message.channel.send("Bem vindo ao Garun BOT!\n")

bot.run(TOKEN)
