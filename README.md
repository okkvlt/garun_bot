# Garun BOT

Um bot de discord para rastrear todas as músicas tocadas em canais de voz e vincular cada uma delas ao last.fm.

## ▪ Como utilizar

Ao utilizar o bot, é primeiro necessário vinculá-lo com sua conta do last.fm.

Para que isso possa ser feito, basta digitar `$connect` e o bot enviará no seu privado todas as instruções.
Após isso, basta ativar o modo scrobbling digitando `$scrobble on`. Caso queira desativar o modo scrobbling, basta digitar `$scrobble off`.

Ademais, o comando `$help` mostrará todas as funções do bot.

<div align="center">
    <img src="https://i.imgur.com/0ee3lTG.png"></img>
</div>

## ▪ Conexão

Como dito, para se conectar, basta digitar `$connect` em qualquer canal de texto [desde que o BOT tenha permissão para leitura] ou na DM.

### ▪ Passo 01

O primeiro passo é clicar no link gerado pelo bot e permitir que o mesmo tenha acesso à sua conta last.fm.

### ▪ Passo 02

O segundo passo é digitar o comando gerado pelo bot e assim criar uma sessão com sua conta last.fm e salvar no banco de dados do bot.

## ▪ Demonstração

<div align="center">
    <div style="display: flex;">
        <img src="https://i.imgur.com/xsXle63.png" width="600"></img>
        <img src="https://i.imgur.com/O0s72Y4.png" width="600"></img>
    </div>
</div>

## ▪ Scrobbling

A opção de scrobbling pode ser ativada digitando `$scrobbling on` e desativada digitando `$scrobbling off`.

O bot permite que o usuário interrompa o scrobble de uma música reagindo à mensagem de scrobbling. Além do mais, o bot também permite que o usuário dê "amei" ou retire o "amei" em uma música também reagindo à mensagem de scrobbling. É claro que o "amei" registrado será encaminhado para a api do last.fm e executado na conta last.fm do usuário.

O "amei" também pode ser dado ou retirado diretamente por comando e para qualquer música, basta digitar `$love [artista] - [música]` para dar o "amei" e `$unlove [artista] - [música]` para retirar o "amei". Um exemplo disso seria `$love Giles Corey - Blackest Bile` ou `$unlove Yung Lean - Ginseng Strip 2002`.

## ▪ Bots Compatíveis

- Hydra;
- Tempo;
- Em breve, mais...

## ▪ Demonstração

<div align="center">
    <img src="https://i.imgur.com/38otbWb.png" width="700"></img>
</div>

## ▪ Charts e Ranks

O bot também conta com a opção de gerar um rank com os artistas ou albums mais escutados por um determinado usuário. Essa opção pode especificar o prazo (por exemplo, nos últimos 7 dias) e o tamanho do rank (por exemplo, top 10).

A syntax para isso é `$top_artists (user) (n) (overall/7day/1month/12month)` para um rank de artistas e `$top_albums (user) (n) (overall/7day/1month/12month)` para um rank de albums.

Exemplo: `$top_artists ruan_1337 15 overall`. Este comando retornará o top _15_ artistas mais escutados pelo usuário _ruan\_1337_ desde a criação de sua conta (_overall_).

## ▪ Demonstração

<div align="center">
    <img src="https://i.imgur.com/podJgp4.png" width="700"></img>
</div>

## ▪ Próximos Updates

- Editar scrobble reagindo à mensagem do bot!
- Player próprio de música!

\~ Coded by okkvlt.
