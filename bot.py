import discord
from decouple import config

bot = discord.Client()

from db import c
from lastfm import controllers
from ready import ready
