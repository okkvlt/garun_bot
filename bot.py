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
    if message.content == "$help":
        message_help = message.channel.send(f"Olá {message.author}! Seja bem vindo ao Garun BOT!\n")
        
        await message_help
    
    if message.author == bot.user and "Seja bem vindo" in message.content:
        await message.add_reaction('❤️')

bot.run(TOKEN)
