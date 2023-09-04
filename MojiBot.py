import asyncio

import discord                          # Documentation: https://discordpy.readthedocs.io/en/stable/index.html
import os

from discord import FFmpegPCMAudio
from dotenv import load_dotenv
from NecoArcASCII import NecoArc
import nacl.secret
import nacl.utils
load_dotenv()                           # Refresh enviroment

# intents are the permissions for the bot
intents = discord.Intents.default()
intents.members = True                  # Detect events related to a server member. For example, a new arrival or someone leaving the server
intents.message_content = True

client=discord.Client(intents=intents)  # After setting the right permissions, send them

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event       # This code block is executed everytime a new member is detected in the server
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    # Writte what to say when a new member joins:
    WelcomeMessage = f'Hello {member.name}! Welcome to the bestest cult ever!'
    # Writte the ID of the channel where to post the welcome message
    welcomechannel = await client.fetch_channel(716613131740381246)
    # To find channel/user/message ID:
    #       https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID
    #       Make sure you get the ID of your channel by right-clicking it and clicking `Copy ID`. Make sure developer mode is on!

    # Once everything ready, post the actual welcome message(s)
    await welcomechannel.send(WelcomeMessage)
    await welcomechannel.send('https://cdn.discordapp.com/attachments/963652712199766106/976170182034718750/Moji_dice_hola.gif')

    #try:
    #    await client.send_message(member, newUserMessage)
    #    print("Sent message to " + member.name)
    #except:
    #    print("Couldn't message " + member.name)
    #embed = discord.Embed(        title="Welcome " + member.name + "!",    description = "We're so glad you're here!",    color = discord.Color.green()    )

    # Assign roles to new members:
    #role = discord.utils.get(member.server.roles, name="name-of-your-role")  # Gets the member role as a `role` object
    #await client.add_roles(member, role)  # Gives the role to the user
    #print("Added role '" + role.name + "' to " + member.name)



@client.event       # This code block is executed everytime a new message is detected
async def on_message(message):
    if message.author == client.user:  # Do not reply to yourself. This line prevents loops
        return

    #if f'{message.author}' == 'anthonyzf20':  # Do not reply to yourself. This line prevents loops
    #    await message.channel.send('¿Quien?')
    #if f'{message.author}' == 'nid6_':
    #    await message.channel.send('Quien?')

    if message.content.lower().startswith('moji, say hello'):
        await message.channel.send('https://cdn.discordapp.com/attachments/963652712199766106/976170182034718750/Moji_dice_hola.gif')
    elif message.content.lower().startswith('moji, dance'):
        await message.channel.send('https://cdn.discordapp.com/attachments/963652712199766106/1147006164689752095/Moji_Dance_-_Bal_Model_sin_clipping.gif')
    elif message.content.lower().startswith('sexo'):
        await message.channel.send('Dont be a pervert, Red. Come on, you made me change the damn code for this')
    elif message.content.lower().startswith('peru'):
        await message.channel.send('Bombardeen Peru')
    elif message.content.lower().startswith('moji, call me daddy'):
        await message.channel.send(f'ok, you are my daddy, {message.author}')
    elif message.content.lower().startswith('moji, fuck me'):
        await message.channel.send(f'No need, goverment already fucks you, {message.author}')
    elif message.content.lower().startswith('5'):
        await message.channel.send(f'Cinco? Por el culo te la ahinco!')
    elif message.content.lower().startswith('thank you, moji'):
        await message.channel.send(f'You are welcome')
    elif message.content.lower().startswith('sorry, moji'):
        await message.channel.send(f'Aww that´s okay!')
    elif message.content.lower().startswith('moji, sleepy time'):
        await message.channel.send(f'Okie Dokie Pokie!')
    elif message.content.lower().startswith('moji, be racist'):
        await message.channel.send(f'Frick em good for nothin Ska´drins!')
    elif message.content.lower().startswith('moji, notify the server'):
        await message.channel.send(f'Okie dokie pokie!')
        await message.channel.send(f'https://cdn.discordapp.com/attachments/902883318679343144/1148389283841966210/7lznjlgopamb1.png')
    # Moji, snack time
    # Good moji
    # Moji, help
    # Calamardo guapo, ASCII


    elif message.content.lower().startswith('moji, scream'):
        if message.author.voice:    # This line checks if the user is in a voice channel
            print(type(message.author.voice))
            channel = message.author.voice.channel
            # They are indeed in a channel, so first, answer the petition
            await message.channel.send(f'Okie doki pokie!')
            await asyncio.sleep(1)
            # Now, lets connect to their channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('scream.mp3'), after=lambda e: print('done', e))
            await asyncio.sleep(2)
            await vc.disconnect()
            print(type(vc))

            #player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
            #player.start()
            #while not player.is_done():
            #    await asyncio.sleep(1)
            # disconnect after the player has finished
            #player.stop()
            #await vc.disconnect()
        else:
            await message.channel.send(f'I dont see you in any voice channel')

    elif message.content.lower().startswith('moji, scream'):
        if message.author.voice:  # This line checks if the user is in a voice channel
            print(type(message.author.voice))
            channel = message.author.voice.channel
            # They are indeed in a channel, so first, answer the petition
            await message.channel.send(f'Okie doki pokie!')
            await asyncio.sleep(1)
            # Now, lets connect to their channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('scream.mp3'), after=lambda e: print('done', e))
            await asyncio.sleep(2)
            await vc.disconnect()
            print(type(vc))

            # player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
            # player.start()
            # while not player.is_done():
            #    await asyncio.sleep(1)
            # disconnect after the player has finished
            # player.stop()
            # await vc.disconnect()
        else:
            await message.channel.send(f'I dont see you in any voice channel')

    elif message.content.lower().startswith('moji, sing'):
        if message.author.voice:    # This line checks if the user is in a voice channel
            print(type(message.author.voice))
            channel = message.author.voice.channel
            # They are indeed in a channel, so first, answer the petition
            await message.channel.send(f'Okie doki pokie!')
            await asyncio.sleep(1)
            # Now, lets connect to their channel
            vc = await channel.connect()
            vc.play(discord.FFmpegPCMAudio('IsabelleSong.mp3'), after=lambda e: print('done', e))
            await asyncio.sleep(194)
            await vc.disconnect()
            print(type(vc))

            #player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
            #player.start()
            #while not player.is_done():
            #    await asyncio.sleep(1)
            # disconnect after the player has finished
            #player.stop()
            #await vc.disconnect()
        else:
            await message.channel.send(f'I dont see you in any voice channel')



    # This one always at the end
    elif message.content.lower().startswith('moji'):
        await message.channel.send(f'Did you call my name?')

    if message.content.lower().startswith('i love you, moji'):
        await message.channel.send(f'Aw :heart: I love you too, {message.author}')


    BluLeibel = f'¿Cuál es el mejor whisky del mundo? ' \
                f'{message.author}, el mejor del mundo es el Blue Label de Johnnie Walker, '\
                f'porque un Johnnie Walker etiqueta negra, lo tomo. Pero cuando es algo especial, tomo un Blue Label. ' \
                f'Es un elixir... y los otros son un whisky. Uno se toma, el otro se saborea!'

    Burrear = \
        f'No sabes lo que es burrear? No le has visto la munda a un burro? Es una vaina de respeto! De fundamento! ' \
        f'Por tanto la chucha de la burra es profunda, cuando yo se lo meto no le hago nada.. pero ella a mi si me hace mucho. ' \
        f'Me succiona la monda y me la pone grande, gruesa y cabezona, una monda de fundamento! de hombre! de varon! ' \
        f'que las venas parecen una avichuela! se le ven como caminito comejen... esa es la diferencia entre tu y yo, ' \
        f'cachaco. Vos con pipi... y yo aca con monda. ' \
        f'Por ende lo que yo le hago a la burra no es zoofilia, es un tratamiento estetico de la monda, ' \
        f'y eso no lo consigues en ni un spa oiste?'

    if message.content.lower().startswith('argentina'):
        await message.channel.send(BluLeibel)
    if message.content.lower().startswith('13'):
        await message.channel.send('Trece? Entre mas me lo mamas mas me crece!!!')
    if message.content.lower().startswith('moji, que es burrear'):
        await message.channel.send(Burrear)


client.run(os.environ['BotToken']) # Bot's unique token, stored in the .env file within the same directory as the rest of the project