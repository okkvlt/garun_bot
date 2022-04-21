from utils.others import getEmbed


async def help_message(message):
    embed = getEmbed()

    embed.add_field(name="Comandos não-Conectados", value="""
• **`$top [modo] [user] [n] [período]`**
• *Mostra o top [n] artistas/artistas mais escutados pelo usuário [user] no período indicado.*

• **Modo:** *'albums', 'artists'*;
• **User:** *last.fm username*;
• **N:** *top [n]*;
• **Período:** *'7day', '1month', '12month', 'overall'*;

• **Exemplo:** *`$top albums ruan_1337 10 7day`*.

• **`$collage [modo] [user] [NxN] [período]`**
• *Gera uma colagem de tamanho [n x n] com os artistas, albums ou músicas mais escutados no período indicado.*

• **Modo:** *'albums', 'artists'*;
• **User:** *last.fm username*;
• **NxN:** *'3x3', '4x4', '5x5', '10x10'*;
• **Período:** *'7day', '1month', '12month', 'overall'*;

• **Exemplo:** *`$collage albums ruan_1337 5x5 overall`*.
""", inline=False)
    
    embed.add_field(name="Comandos Conectados", value="""
• `$scrobble [on/off]` 
• *Ativa ou desativa os scrobbles.*

• `$love [artist] - [track]`
• *Dá "amei" na música informada.*

• `$unlove [artist] - [track]` 
• *Retira o "amei" da música informada.*
""", inline=False)
    
    embed.add_field(name="Comandos de Conexão", value="""
• `$connect`
• *Vincula o bot à sua conta do last.fm.*

• `$disconnect`
• *Desconecta a conta.*
""", inline=False)

    return await message.channel.send(embed=embed)
