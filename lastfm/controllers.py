from config.bot import bot
from config.config import HYDRA, TEMPO, CHIP

from lastfm.auth import auth, disconnect, session
from lastfm.collage import collage
from lastfm.help import help_message
from lastfm.love import love_track
from lastfm.reactions import check_reactions, reaction
from lastfm.scrobble import (chip, hydra, scrobble_after_delete, scrobble_on_off,
                             tempo)
from lastfm.top import top


@bot.event
async def on_message(message):
    controllers = {
        "content": {
            "$top": top,
            "$connect": auth,
            "$session": session,
            "$scrobble": scrobble_on_off,
            "$disconnect": disconnect,
            "$help": help_message,
            "$love": love_track,
            "$unlove": love_track,
            "$collage": collage
        },

        "author": {
            HYDRA: hydra,
            TEMPO: tempo,
            CHIP: chip,
            bot.user.id: reaction
        }
    }

    author = message.author.id

    if author in controllers["author"].keys():
        control_function = controllers["author"][author]
        return await control_function(message)

    if not message.content:
        return

    msg = message.content.split()
    command = msg[0]

    if not command in controllers["content"].keys():
        return

    control_function = controllers["content"][command]
    return await control_function(message)


@bot.event
async def on_reaction_add(reaction, user):
    if reaction.message.author.id == bot.user.id:
        return await check_reactions(reaction, user, 1)


@bot.event
async def on_reaction_remove(reaction, user):
    if reaction.message.author.id == bot.user.id:
        return await check_reactions(reaction, user, 2)


@bot.event
async def on_message_delete(message):
    if message.author.id == bot.user.id:
        return await scrobble_after_delete(message)
