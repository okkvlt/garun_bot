import discord
from decouple import config
from collage.collage import LastFM

# discord
TOKEN = config('BOT_TOKEN')

# last.fm api
API_KEY = config('API_KEY')
API_SECRET = config('API_SECRET')

# database
DB = "config/sessions.db"

# bots
HYDRA = 547905866255433758
TEMPO = 736888501026422855

# intents
INTENTS = discord.Intents.default()

INTENTS.members = True
INTENTS.reactions = True

# collage
COLLAGE = LastFM(API_KEY)
