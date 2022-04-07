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
        embed_help = discord.Embed(colour=0xedd58d)

        embed_help.set_author(name="Garun — Help",
                              icon_url='https://i.imgur.com/59qD9SY.jpg')

        embed_help.add_field(name="Comandos de DJ", value="""
`$play (music/playlist)` — *reproduz a música ou a playlist.*
`$queue` — *mostra lista de reprodução.*
`$pause` — *pausa a música.*
`$resume` — *despausa a música.*
`$stop` — *para de reproduzir.*
`$next` — *avança para a próxima música.*
`$back` — *retorna para a música anterior.*
`$shuffle` — *ativa ordem aleatória.*
`$goto (n)` — *avança ou retorna para a música da posição n da lista de reprodução.*
`$clear` — *limpa a lista de reprodução.*
`$add (music/playlist)` — *adiciona música ou playlist na lista de reprodução.*
`$remove (n)` — *remove música da posição n da lista de reprodução.*
""", inline=False)

        embed_help.add_field(name="Comandos de LAST.FM", value="""
`$connect` — *conecta do last.fm com o bot.*
`$scrobble (on/off)` — *ativa ou desativa os scrobbles.*
`$edit` — *edita os dados do scrobble em execução.*
`$skip` — *interrompe o scrobble em execução.*
`$disconnect` — *desconecta a conta.*
""", inline=False)

        embed_help.set_footer(
            text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

        await message.channel.send(embed=embed_help)

bot.run(TOKEN)
