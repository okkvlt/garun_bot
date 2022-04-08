import discord
from bot import bot


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
`$top_artists (user) (n) (overall/7day/1month/12month)` — *mostra o top (n) artistas do usuário no(s) último(s) (overall/7day/1month/12month).*
`$top_albums (user) (n) (overall/7day/1month/12month)` — *mostra o top (n) albums do usuário no(s) último(s) (overall/7day/1month/12month).*
`$scrobble (on/off)` — *ativa ou desativa os scrobbles.*
`$edit` — *edita os dados do scrobble em execução.*
`$skip` — *interrompe o scrobble em execução.*
`$collage (artists/albums) (7/30)` — *gera uma colagem com os artistas ou albums mais ouvidos nos últimos sete ou trinta dias.*
`$disconnect` — *desconecta a conta.*
""", inline=False)

        embed_help.set_footer(
            text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

        await message.channel.send(embed=embed_help)
