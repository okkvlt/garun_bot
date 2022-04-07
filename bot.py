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
        
        help_message = f"""
Olá {message.author}! Seja bem vindo ao Garun BOT!

Segue a lista de comandos para o uso do bot:

$help: mostra essa mensagem;

DJ:

$play [spotify music/playlist]: reproduz a música ou playlist passada por argumento;
$queue: mostra a lista de reprodução;
$pause: pausa a reprodução;
$resume: despausa a reprodução;
$stop: desconecta o bot da call;
$next: avança para a próxima música;
$back: retorna para a música passada;
$goto [n]: avança ou retorna para a música da posição n da lista;
$clear: limpa a lista de reprodução;
$add [spotify music/playlist]: adiciona música ou playlist na lista de reprodução;
$remove [n]: remove a música da posição n da lista;
$volume [0-100]: altera o volume do bot;

LAST.FM:

$connect: conecta o BOT com sua conta do last.fm;
$scrobble [on/off]: ativa/desativa o modo scrobble;
$edit: edita os dados do scrobble em execução;
$skip: interrompe o scrobble em execução;
$disconnect: desconecta o BOT da sua conta do last.fm;
"""
        
        message_help = message.channel.send(help_message)
        
        await message_help
    
    if message.author == bot.user and "Seja bem vindo" in message.content:
        await message.add_reaction('❤️')
        await message.add_reaction('🕊️')

bot.run(TOKEN)
