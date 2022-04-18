from utils.others import getEmbed


async def help_message(message):
    embed = getEmbed()

    embed.add_field(name="Comandos de LAST.FM", value="""
• `$connect`
• *Vincula o bot à sua conta do last.fm.*

• `$top_artists (user) (n) (overall/7day/1month/12month)`
• *Mostra o top (n) artistas do usuário (user) no(s) último(s) (overall/7day/1month/12month).*

• `$top_albums (user) (n) (overall/7day/1month/12month)`
• *Mostra o top (n) albums do usuário no(s) último(s) (overall/7day/1month/12month).*

• `$scrobble (on/off)` 
• *Ativa ou desativa os scrobbles.*

• `$edit`
• *Edita os dados do scrobble em execução.* [não implementado]

• `$stop`
• *Interrompe o scrobble em execução.* [não implementado]

• `$love "(artist) - (track)"`
• *Dá "amei" na música informada.*

• `$unlove "(artist) - (track)"` 
• *Retira o "amei" da música informada.*

• `$collage (artists/albums) (7/30)`
• *Gera uma colagem com os artistas ou albums mais ouvidos nos últimos sete ou trinta dias.* [não implementado]

• `$disconnect`
• *Desconecta a conta.*
""", inline=False)

    await message.channel.send(embed=embed)
