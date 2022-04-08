import discord
from decouple import config

bot = discord.Client()

from ready import ready
from commands import help
from commands.last import controllers