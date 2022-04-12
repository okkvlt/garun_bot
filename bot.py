import sqlite3

import discord
from decouple import config

bot = discord.Client()

from commands.last import controllers
from db import c
from ready import ready
