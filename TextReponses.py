import asyncio
import json
import random
from pathlib import Path
import discord

# Obtenemos el directorio actual donde nos encontramos
current_dir = str(Path(__file__).resolve().parent).replace('\\', '/')

def RockPaperScissors (Attack):
    Defense = random.randint(0, 2)

    if   Attack == 'scissors':
        if   Defense == 0: return f'Paper! Aw, I lost!'
        elif Defense == 1: return f'Scissors! a tie?'
        elif Defense == 2: return f'Rock! I win!'
    elif Attack == 'paper':
        if   Defense == 0: return f'Rock! Aw, I lost!'
        elif Defense == 1: return f'Paper! a tie?'
        elif Defense == 2: return f'Scissors! I win!'
    elif   Attack == 'rock':
        if   Defense == 0: return f'Scissors! Aw, I lost!'
        elif Defense == 1: return f'Rock! a tie?'
        elif Defense == 2: return f'Paper! I win!'

async def Responses(message, client): #arguments:
        # Open the JSON file with the list of reponses
        with open(current_dir + '/QuickResponses.json', 'r') as openfile:
            ResponsesList = json.load(openfile)

        # Dump the info of said file into a dictionary
        Replies = ResponsesList
        Close = False
        for key in Replies:
            if message.content.lower().startswith(f'{key}'):
                await message.channel.send(f'{Replies[key]}')
                Close = True

        if Close: return

        #"Calamardo guapo, ASCII"

        if message.content.lower().startswith('moji, help'):
            await message.channel.send(f'This is a list of some of the phrases that I respond to. '
                                       f'I do not care about lowercase or uppercase')
            HelpList = f''
            for key in Replies:
                HelpList = HelpList + f'- {key}\n'
            HelpList = HelpList + f'- moji, scream\n' \
                                  f'moji, sing\n' \
                                  f'moji, rock\n' \
                                  f'moji, paper\n' \
                                  f'moji, scissors\n'
            await message.channel.send(HelpList)

        elif message.content.lower().startswith('moji, scream') and False:
            if message.author.voice:  # This line checks if the user is in a voice channel
                channel = message.author.voice.channel
                # They are indeed in a channel, so first, answer the petition
                await message.channel.send(f'Okie doki pokie!')
                await asyncio.sleep(1)
                # Now, lets connect to their channel
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('AudioFiles/scream.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(2)
                await vc.disconnect()

                # player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
                # player.start()
                # while not player.is_done():
                #    await asyncio.sleep(1)
                # disconnect after the player has finished
                # player.stop()
                # await vc.disconnect()
            else:
                await message.channel.send(f'I dont see you in any voice channel')
        elif message.content.lower().startswith('moji, sing') and False:
            if message.author.voice:  # This line checks if the user is in a voice channel
                print(type(message.author.voice))
                channel = message.author.voice.channel
                # They are indeed in a channel, so first, answer the petition
                await message.channel.send(f'Okie doki pokie!')
                await asyncio.sleep(1)
                # Now, lets connect to their channel
                vc = await channel.connect()
                vc.play(discord.FFmpegPCMAudio('AudioFiles/IsabelleSong.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(194)
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

        elif message.content.lower().startswith('moji, rock'):
            if f'{message.author}' == 'anthonyzf20':    await message.channel.send('Paper! I win!')
            else:                                       await message.channel.send( RockPaperScissors('rock'))
        elif message.content.lower().startswith('moji, paper'):
            if f'{message.author}' == 'anthonyzf20':    await message.channel.send('Scissors! I win!')
            else:                                       await message.channel.send( RockPaperScissors('paper'))
        elif message.content.lower().startswith('moji, scissors'):
            if f'{message.author}' == 'anthonyzf20':    await message.channel.send('Rock! I win!')
            else:                                       await message.channel.send( RockPaperScissors('scissors'))

        elif message.content.lower().startswith('moji, what is the most compatible race'):
            await message.channel.send(f'In terms of humanoid and not-humanoid inter-breeding, leiporis are the most '
                                 f'compatible race for humans and elves. \n\nNot only are they descendants of '
                                 f'rabbit-like beings, which are mammals, leiporis can change their own size through '
                                 f'magic. This means that they can be large enough to be able to handle any dick size, '
                                 f'and with their impresive healing magic, you can be rough with one. '
                                 f'Some leiporis can also use water-based magic, so there is no doubt in my mind that '
                                 f'an aroused leipori would be incredible wey, so wet in fact that you could easily '
                                 f'have sex with one for hours without getting sore. They also have mastery of '
                                 f'polymorph magic, so it would be incredibly easy for one to seduce you through '
                                 f'shapeshifting to get you in the mood. Furthermore, with their rabbit-like '
                                 f'endurance, they dont get tired easily. No other race comes close to this level of '
                                 f'compatibility. Also, fun fact, a rabbit´s jump speed is between 25 and 40 mph, so '
                                 f'one leipori could ride your dick at unhuman speeds. Leiporis are literally built '
                                 f'for dick. \n\nUngodly healing + high endurance + polymorph magic means they can '
                                 f'take dick all day, all shapes andsizes and still come for more')
        elif message.content.lower().startswith('argentina'):
            await message.channel.send( f'¿Cuál es el mejor whisky del mundo? {message.author}, el mejor del mundo es '
                                        f'el Blue Label de Johnnie Walker, porque un Johnnie Walker etiqueta negra, '
                                        f'lo tomo. Pero cuando es algo especial, tomo un Blue Label. Es un elixir... '
                                        f'y los otros son un whisky. Uno se toma, el otro se saborea!')
        elif message.content.lower().startswith('moji, que es burrear'):
            await message.channel.send( f'No sabes lo que es burrear? No le has visto la munda a un burro? Es una '
                                        f'vaina de respeto! De fundamento! Por tanto la chucha de la burra es '
                                        f'profunda, cuando yo se lo meto no le hago nada.. pero ella a mi si me hace '
                                        f'mucho. Me succiona la monda y me la pone grande, gruesa y cabezona, una '
                                        f'monda de fundamento! de hombre! de varon! que las venas parecen una '
                                        f'habichuela! se le ven como caminito comejen... esa es la diferencia entre tu '
                                        f'y yo, cachaco. Vos con pipi... y yo aca con monda. Por ende lo que yo le '
                                        f'hago a la burra no es zoofilia, es un tratamiento estetico de la monda, y '
                                        f'eso no lo consigues en ni un spa oiste?')
        elif message.content.lower().startswith('moji'):
            await message.channel.send(f'Did you call my name?')