from utils.others import get_top, getEmbed


async def top(message):
    data = message.content.split()

    fail = getEmbed()
    sucess = getEmbed()

    fail.add_field(name="Status",
                   value="*Formato inválido!*",
                   inline=False)

    fail.add_field(name="Syntax:",
                   value="*`$top [modo] [user] [n] [período]`*",
                   inline=False)
    
    fail.add_field(name="Params:",
                   value="""
                    • **[modo]:** *'albums', 'artists'*;
                    • **[user]:** *last.fm username*;
                    • **[n]:** *top [n]*;
                    • **[período]:** *'7day', '1month', '12month', 'overall'*;
                   """,
                   inline=False)

    modes = {
        "artists": 1,
        "albums": 2
    }
    
    periods = ["overall", "7day", "1month", "12month"]

    if len(data) != 5:
        return await message.channel.send(embed=fail)

    mode = data[1]
    user = data[2]
    size = data[3]
    period = data[4]

    if not mode in modes:
        return await message.channel.send(embed=fail)

    if not period in periods:
        return await message.channel.send(embed=fail)

    r = get_top(user, size, period, modes[mode])

    if "error" in r:
        return

    if mode == "albums":
        top = r["topalbums"]["album"]

        sucess.set_author(name="Garun — Top "+size+" albums",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    else:
        top = r["topartists"]["artist"]

        sucess.set_author(name="Garun — Top "+size+" artistas",
                          icon_url='https://i.imgur.com/59qD9SY.jpg')

    if not top:
        return

    value = ""

    if mode == "albums":
        for album in top:
            value += "**"+album["@attr"]["rank"]+"º**: *"+album["artist"]["name"] + \
                " — " + album["name"]+" ("+album["playcount"]+" plays).*\n"

    else:
        for artist in top:
            value += "**"+artist["@attr"]["rank"]+"º** — *" + \
                artist["name"]+" ("+artist["playcount"]+" plays).*\n"

    sucess.add_field(name="Usuário: ",
                     value="`"+user+"`",
                     inline=False)

    if mode == "albums":
        sucess.add_field(name="Top " + str(size) +
                         " albums", value=value, inline=False)
    else:
        sucess.add_field(name="Top " + str(size) +
                         " artistas", value=value, inline=False)

    return await message.channel.send(embed=sucess)
