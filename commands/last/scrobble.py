from psycopg2 import Timestamp
import discord
import time
from bot import bot
from commands.last.utils import scrobbleTrack

async def scrobble(message):
    artist = "Yung Lean"
    track = "Ginseng Strip 2002"
    timestamp = int(time.time())
    
    return await message.channel.send(embed=scrobbleTrack(message, artist, track, timestamp))