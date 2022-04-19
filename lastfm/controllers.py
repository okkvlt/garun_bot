import discord
import time
from config.bot import bot

from lastfm.auth import auth, disconnect, session
from lastfm.help import help_message
from lastfm.love import love_track
from lastfm.scrobble import hydra, reaction, scrobble, tempo
from lastfm.top import top

from utils.others import nowPlaying_and_Scrobble
from utils.database import get_scrobblers


@bot.event
async def on_message(message):
    if "$top_artists" in message.content:
        return await top(message, 2)

    if "$top_albums" in message.content:
        return await top(message, 1)

    if message.content == "$connect":
        return await auth(message)

    if "$session" in message.content:
        return await session(message)

    if "$scrobble" in message.content:
        return await scrobble(message)

    if message.content == "$disconnect":
        return await disconnect(message)

    if message.author.id == 547905866255433758: ##HYDRA ID
        return await hydra(message)

    if message.content == "$help":
        return await help_message(message)

    if "$love" in message.content:
        return await love_track(message, 1)

    if "$unlove" in message.content:
        return await love_track(message, 2)

    if message.author.id == 736888501026422855: ##TEMPO ID
        return await tempo(message)

    if message.author.id == bot.user.id: ##GARUN ID
        return await reaction(message)
    
    
@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author.id == bot.user.id:
        print(reaction)
        print(user)
        
@bot.event
async def on_message_delete(message):
    if message.author.id == bot.user.id:
        for embed in message.embeds:
            content = embed.to_dict()
            status = content["fields"][0]["value"]
            
            if status == "*Scrobbling...!*":
                artist = content["fields"][1]["value"]
                track = content["fields"][2]["value"]
                
                timestamp = int(time.time())

                scrobblers = get_scrobblers()

                if len(scrobblers) > 0:
                    return await message.channel.send(embed=nowPlaying_and_Scrobble(scrobblers, artist, track, timestamp, 2),
                                                      delete_after=60)