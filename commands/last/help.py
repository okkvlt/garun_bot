import discord
from bot import bot


@bot.event
async def help_(message):
    embed_help = discord.Embed(colour=0xedd58d)

    embed_help.set_author(name="Garun — Help",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    embed_help.add_field(name="Comandos de LAST.FM", value="""
`$connect` — *conecta do last.fm com o bot.*
`$top_artists (user) (n) (overall/7day/1month/12month)` — *mostra o top (n) artistas do usuário no(s) último(s) (overall/7day/1month/12month).*
`$top_albums (user) (n) (overall/7day/1month/12month)` — *mostra o top (n) albums do usuário no(s) último(s) (overall/7day/1month/12month).*
`$scrobble (on/off)` — *ativa ou desativa os scrobbles.*
`$edit` — *edita os dados do scrobble em execução.* [não implementado]
`$stop` — *interrompe o scrobble em execução.* [não implementado]
`$love` — *dá "amei" na música em execução.* [não implementado]
`$unlove` — *retira o "amei" da música em execução.* [não implementado]
`$collage (artists/albums) (7/30)` — *gera uma colagem com os artistas ou albums mais ouvidos nos últimos sete ou trinta dias.* [não implementado]
`$disconnect` — *desconecta a conta.*
""", inline=False)

    embed_help.set_footer(
        text=f"Powered by {bot.user}", icon_url='https://i.imgur.com/59qD9SY.jpg')

    await message.channel.send(embed=embed_help)
