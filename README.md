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

A opção de scrobbling pode ser ativada digitando `$scrobble on` e desativada digitando `$scrobble off`.

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

## ▪ Ranks

O bot também conta com a opção de gerar um rank em formato de texto com os artistas ou albums mais escutados por um determinado usuário. Essa opção pode especificar o prazo (por exemplo, nos últimos 7 dias) e o tamanho do rank (por exemplo, top 10). 

### Syntax:
- _`$top [modo] [user] [n] [período]`_.
    - [modo]: _"artists"_, _"albums"_;
    - [user]: _last.fm username_;
    - [n]: _top \[n\]_;
    - [período]: _7day, 1month, 12month, overall_.

### Exemplo: 
- _`$top artists ruan_1337 15 overall`_: Este comando retornará o top _15_ _artistas_ mais escutados pelo usuário _ruan\_1337_ desde a criação de sua conta (_overall_).

## ▪ Demonstração

<div align="center">
    <img src="https://i.imgur.com/FoQNOfQ.png" width="600"></img>
</div>

## ▪ Colagem

Apesar de conter uma opção que gera um rank em formato de texto com os albums ou artistas mais escutados por um determinado usuário em um determinado período de tempo, o bot também possui uma função capaz de gerar o mesmo rank em formato de imagem/colagem. O código para a geração das colagens foi escrito por [@iShi0n](https://github.com/iShi0n).

### Syntax:
- _`$collage [modo] [user] [NxN] [período]`_.
    - [modo]: _"artists"_, _"albums"_;
    - [user]: _last.fm username_;
    - [NxN]: _3x3, 4x4, 5x5, 10x10_;
    - [período]: _7day, 1month, 12month, overall_.

### Exemplos: 
- `$collage albums ruan_1337 5x5 7day`: Gera uma colagem de tamanho _5x5_ com os _albums_ mais escutados por _ruan\_1337_ nos últimos 7 dias _(7day)_.
- `$collage artists ruan_1337 10x10 overall`: Gera uma colagem de tamanho _10x10_ com os _artistas_ mais escutados por _ruan\_1337_ desde a criação de sua conta _(overall)_.

## ▪ Demonstração

<div align="center">
    <div style="display: flex;">
        <img src="https://i.imgur.com/sIQy5GA.png" width="600"></img>
        <img src="https://i.imgur.com/XYbabQS.png" width="600"></img>
    </div>
</div>

## ▪ Próximos Updates

- Editar scrobble reagindo à mensagem do bot!
- Player próprio de música!

\~ Coded by okkvlt.
