import discord

from config.config import INTENTS

bot = discord.Client(intents=INTENTS)

from lastfm import controllers
from ready import ready

from config.db import c
