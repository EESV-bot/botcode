import discord
from discord.ext import commands
import random
import asyncio
import json

client = commands.Bot(command_prefix='.')
client.remove_command('help')

#
#
#
#     ,---,.                                  ___
#   ,'  .' |                                ,--.'|_
# ,---.'   |                        ,---,   |  | :,'   ,---.
# |   |   .'     .---.          ,-+-. /  |  :  : ' :  '   ,'\   .--.--.
# :   :  |-,   /.  ./|  ,---.  ,--.'|'   |.;__,'  /  /   /   | /  /    '
# :   |  ;/| .-' . ' | /     \|   |  ,"' ||  |   |  .   ; ,. :|  :  /`./
# |   :   .'/___/ \: |/    /  |   | /  | |:__,'| :  '   | |: :|  :  ;_
# |   |  |-,.   \  ' .    ' / |   | |  | |  '  : |__'   | .; : \  \    `.
# '   :  ;/| \   \   '   ;   /|   | |  |/   |  | '.'|   :    |  `----.   \
# |   |    \  \   \  '   |  / |   | |--'    ;  :    ;\   \  /  /  /`--'  /
# |   :   .'   \   \ |   :    |   |/        |  ,   /  `----'  '--'.     /
# |   | ,'      '---" \   \  /'---'          ---`-'             `--'---'
# `----'               `----'
#
#   By: lnstrument


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game(".help #EESV"))
    print('Bot prendido, by lnstrument EESV')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Se han dado pocos argumentos. Para más ayuda, utiliza ``.help``')


@client.event
async def on_member_join(ctx, member: discord.Member):
    await ctx.send(f'{member} ha entrado al servidor.')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name = '「👋﹡bienvenidas')
    d = [f" ╬ ¡Bienvenido {member} a EESV Official Group! ╬",
        f"  ╬ ¡Atención, {member} ha entrado al servidor!  ╬"
         ]
    await channel.send(random.choice(d))




#
#
#
#                              ____
#                            ,'  , `.                             ,---,
#             ,---.       ,-+-,.' _ |                 ,---,     ,---.'|   ,---.
#            '   ,'\   ,-+-. ;   , ||             ,-+-. /  |    |   | :  '   ,'\   .--.--.
#    ,---.  /   /   | ,--.'|'   |  || ,--.--.    ,--.'|'   |    |   | | /   /   | /  /    '
#   /     \.   ; ,. :|   |  ,', |  |,/       \  |   |  ,"' |  ,--.__| |.   ; ,. :|  :  /`./
#  /    / ''   | |: :|   | /  | |--'.--.  .-. | |   | /  | | /   ,'   |'   | |: :|  :  ;_
# .    ' / '   | .; :|   : |  | ,    \__\/: . . |   | |  | |.   '  /  |'   | .; : \  \    `.
# '   ; :__|   :    ||   : |  |/     ," .--.; | |   | |  |/ '   ; |:  ||   :    |  `----.   \
# '   | '.'|\   \  / |   | |`-'     /  /  ,.  | |   | |--'  |   | '/  ' \   \  /  /  /`--'  /
# |   :    : `----'  |   ;/        ;  :   .'   \|   |/      |   :    :|  `----'  '--'.     /
#  \   \  /          '---'         |  ,     .-./'---'        \   \  /              `--'---'
#   `----'                          `--`---'                  `----'
#
#
#  By: lnstrument

#
#   Ping
#
@client.command()
async def ping(ctx):
    await ctx.send(f'``Pong! {round(client.latency * 1000)}ms``')


#
#   8ball
#
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['¡Claro que sí!',
                 'Obviamente.',
                 'Sí.',
                 'Creo que sí...',
                 'Posiblemente.',
                 'No.',
                 'Obviamente no.',
                 '¿Tú crees?',
                 'Claro que no.',
                 'Ni en sueños.',
                 'Tal vez.']
    await ctx.send(f'```Pregunta: {question}\nRespuesta: {random.choice(responses)}```')


#
#   Clear
#
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=1):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
#   Nuke
#
@client.command()
@commands.has_permissions(manage_messages=True)
async def nuke(ctx, amount=5000000):
    await ctx.channel.purge(limit=amount)
    await ctx.send(
        'Nuke con éxito. :exploding_head: https://media.tenor.com/images/c243489a85b9ab833012da3acfec815b/tenor.gif ')

@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
#   Kick
#
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} ha sido kickeado por: ``{reason}``.')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
# Ban
#
@client.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} ha sido baneado por: ``{reason}``.')

@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
# Unban
#
@client.command()
@commands.has_permissions(ban_members=True, kick_members=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} ha sido unbaneado.')
            return

@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
#   Mute
#
@client.command()
@commands.has_permissions(kick_members=True)
async def mute(ctx, member: discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.add_roles(role)
            await ctx.send("{} ha muteado a {}".format(member.mention, ctx.author.mention))
            return

            overwrite = discord.PermissionsOverwrite(send_messages=False)
            newRole = await guild.create_role(name="Muted")

            for channel in guild.text_channels:
                await channel.set_permissions(newRole, overwrite=overwrite)

            await member.add_roles(newRole)
            await ctx.send("{} ha sido muteado por {}.".format(member.mention, ctx.author.mention))

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
#   Unmute
#
@client.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    guild = ctx.guild

    for role in guild.roles:
        if role.name == "Muted":
            await member.remove_roles(role)
            await ctx.send("{} ha sido unmuteado por {}".format(member.mention, ctx.author.mention))
            return

@unmute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("** :no_entry_sign: No tienes los permisos suficientes. :no_entry_sign: **")


#
#   Help
#
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Colour.orange()
    )

    embed.set_author(name='Comandos de EESV Official Bot')
    embed.add_field(name='.help', value='Te envía este mensaje a tus mensajes directos.', inline=False)
    embed.add_field(name='.discord', value='Invitación al servidor oficial de EESV.', inline=False)
    embed.add_field(name='.creditos', value='Creador del bot.', inline=False)
    embed.add_field(name='.say', value='El bot enviará tu mensaje anonimamente. ``.say <mensaje>``', inline=False)
    embed.add_field(name='.coinflip', value='Cara o cruz.', inline=False)
    embed.add_field(name='.ping', value='Pong!', inline=False)
    embed.add_field(name='.8ball', value='``.8ball <pregunta>``', inline=False)
    embed.add_field(name='.avatar', value='Foto de perfil de un usuario.``.avatar <@usuario>``', inline=False)
    embed.add_field(name='.userinfo', value='Información de un usuario.``.userinfo <@usuario>``', inline=False)
    embed.add_field(name='.clear', value='Elimina mensajes dependiendo la cantidad. ``.clear <cantidad>``', inline=False)
    embed.add_field(name='.nuke', value='Elimina todos los mensajes del chat.', inline=False)
    embed.add_field(name='.mute', value='Mutear a un usuario. ``.mute <@usuario>``', inline=False)
    embed.add_field(name='.unmute', value='Remover mute a un usuario. ``.unmute <@usuario>``', inline=False)
    embed.add_field(name='.kick', value='Kickear a un usuario del servidor. ``.kick <@usuario> <razón>``', inline=False)
    embed.add_field(name='.ban', value='Banear a un usuario del servidor. ``.ban <@usuario> <razón>``', inline=False)
    embed.add_field(name='.unban', value='Remover ban a un usuario. ``.unban <@usuario>``', inline=False)



    await author.send(embed=embed)


#
#   Userinfo
#
@client.command()
async def userinfo(ctx, member: discord.Member):
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Pedido por {ctx.author}", icon_url=ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nombre:", value=member.display_name)

    embed.add_field(name="Fecha de creación:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Fecha de ingreso al servidor:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
    embed.add_field(name="Role más alto:", value=member.top_role.mention)

    embed.add_field(name="Bot?", value=member.bot)

    await ctx.send(embed=embed)


#
#   Avatar
#
@client.command()
async def avatar(ctx, member: discord.Member):
    show_avatar = discord.Embed(

        color = discord.Colour.orange()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)


#
#   Coinflip
#
@client.command()
async def coinflip(ctx):
    choices = ("**Cara** https://rollthedice.online/assets/images/upload/dice/dado-cara-cruz/cara_moneda.png", "**Cruz** https://rollthedice.online/assets/images/upload/dice/dado-cara-cruz/cruz_moneda.png")
    rancoin = random.choice(choices)
    await ctx.send(rancoin)


#
#   Say
#
@client.command()
async def say(ctx, *, msg):
    await ctx.message.delete()
    await ctx.send("{}".format(msg))


@client.command()
async def creditos(ctx):
    await ctx.send(f'Créditos a lnstrument y Marka. lnstrument creador del bot, Marka hosteo del bot. Los más facha del universo. :sunglasses:')


@client.command()
async def alejo(ctx):
    await ctx.send('Acabas de mencionar al mas pro juaker c++ ddos gamer de toda EESV. :heart_eyes: ')


@client.command()
async def discord(ctx):
    await ctx.send('**Discord Oficial EESV** https://discord.gg/5txZjDR')


client.run('Token del Bot')