import discord
from decouple import config


TOKEN = config('BOT_TOKEN')

bot = discord.Client()

from commands import help
from ready import ready