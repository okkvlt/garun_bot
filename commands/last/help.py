import discord
from bot import bot


async def help_message(message):
    embed_help = discord.Embed(colour=0xedd58d)

    embed_help.set_author(name="Garun — Help",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    embed_help.add_field(name="Comandos de LAST.FM", value="""
`$connect` — *Conecta do last.fm com o bot.*
`$top_artists (user) (n) (overall/7day/1month/12month)` — *Mostra o top (n) artistas do usuário no(s) último(s) (overall/7day/1month/12month).*
`$top_albums (user) (n) (overall/7day/1month/12month)` — *Mostra o top (n) albums do usuário no(s) último(s) (overall/7day/1month/12month).*
`$scrobble (on/off)` — *Ativa ou desativa os scrobbles.*
`$edit` — *Edita os dados do scrobble em execução.* [não implementado]
`$stop` — *Interrompe o scrobble em execução.* [não implementado]
`$love [music_id]` — *Dá "amei" na música em execução.* [não implementado]
`$unlove [music_id]` — *Retira o "amei" da música em execução.* [não implementado]
`$collage (artists/albums) (7/30)` — *Gera uma colagem com os artistas ou albums mais ouvidos nos últimos sete ou trinta dias.* [não implementado]
`$disconnect` — *Desconecta a conta.*
""", inline=False)

    embed_help.set_footer(
        text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

    await message.channel.send(embed=embed_help)
