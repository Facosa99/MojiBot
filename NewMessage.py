import asyncio
import json
from pathlib import Path
from RockPaperScissors import RockPaperScissors
import discord

# Current directory
current_dir = str(Path(__file__).resolve().parent).replace('\\', '/')

async def Responses(message, client):

        # if f'{message.author}' == 'anthonyzf20':  # Reply to this user everytime the bot detects a new message from then
        #    await message.channel.send('¿Quien?')
        #   return


        # Open the JSON file with the list of simple text replies
        with open(current_dir + '/QuickResponses.json', 'r') as openfile:
            ResponsesList = json.load(openfile)

        # Dump the info of said file into a dictionary
        Replies = ResponsesList
        Close = False

        # Check if we hit any of the JSON replies
        for key in Replies:
            if message.content.lower().startswith(f'{key}'):
                Replies[key] = Replies[key].replace("(user.name)", f'{message.author}')
                await message.channel.send(f'{Replies[key]}')
                Close = True
            if Close: return    # If we hit the target phrase already, there is no need to run the rest of the for loop nor the rest of this function

        # If we didnt trigger any simple text reply, is time to check for the slighty more interactive ones
        if message.content.lower().startswith('moji, help'):
            await message.channel.send(f'This is a list of some of the phrases that I respond to. '
                                       f'I do not care about lowercase or uppercase')
            HelpList = f''
            for key in Replies:
                HelpList = HelpList + f'- {key}\n'

            # We append the phrases that arent included in the JSON file
            HelpList = HelpList + f'- moji, scream\n' \
                                  f'- moji, sing\n' \
                                  f'- moji, rock\n' \
                                  f'- moji, paper\n' \
                                  f'- moji, scissors\n'
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
        return