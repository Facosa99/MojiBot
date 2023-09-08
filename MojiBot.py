import asyncio
import discord                          # Documentation: https://discordpy.readthedocs.io/en/stable/index.html
import os
from dotenv import load_dotenv
from discord.ext import commands
import json
from pathlib import Path

# Local Libraries
from NewMessage import Responses
from NewMember import AutomaticWelcome
from RockPaperScissors import RockPaperScissors

load_dotenv()                           # Refresh enviroment
current_dir = str(Path(__file__).resolve().parent).replace('\\', '/')   # Directory from which the program is executed/stored

# intents are the permissions for the bot
intents = discord.Intents.default()
intents.members = True                  # Detect events related to a server member. For example, a new arrival or someone leaving the server
intents.message_content = True          # Detects messages and their content, name is pretty self explanatory

bot = commands.Bot(command_prefix = ('Moji, ', 'moji, '), intents=intents, help_command=None)  # Set the prefix and the permissions.

@bot.event       # This code block is executed once, after the Bot logins
async def on_ready():
    print(f'We have logged in as {bot.user}')
    return
@bot.event       # This code block is executed everytime a new member joins the server
async def on_member_join(member):
    await AutomaticWelcome(member, bot)
    return
@bot.event       # This code block is executed everytime a new message is detected
async def on_message(message):
    if f'{message.author}' == 'facosa99' and message.content.lower().startswith('moji, update commands'):
        # await bot.tree.sync()
        await message.channel.send('"bot.tree.sync()" is temporaily disabled, master')
        return

    if message.author == bot.user: return   # if current message is from Bot itself, ignore it and finish the function.
                                            # This prevents the bot from replying to itself and thus avoids undesirable loops.

    await Responses(message, bot)           # If you want simple responses to certain messages, set them in the associated JSON
                                            # file and put this line. For more interactive responses (like repeating the message
                                            # text or doing an operation) use commands, as those can receive arguments

    await bot.process_commands(message)     # Check if received message is a command
                                            # If your bot has no commands, then this line isnt necesary. Also you might want to change
                                            # from "bot" to "client". Setting it as "bot" is only necesary for enabling commands
    return

# -------------------------------------List of all available commands---------------------------------------------------
@bot.command(name='say', help="Makes Moji say whatever you want")
async def say(ctx, *arg):
    Text = " ".join(arg)
    await ctx.send(f"{Text}")
    await ctx.message.delete()
    return

@bot.command(name='help', help="Gotta get this shit running")
async def help(ctx):
    # Open the JSON file with the list of simple text replies
    with open(current_dir + '/QuickResponses.json', 'r') as openfile:
        ResponsesList = json.load(openfile)

    Replies = ResponsesList # Dump the info of said file into a dictionary
    ResponsesList.close()   # The info has been dumped into the dictionay, JSON can be closed now.

    # Create a String to store our reply to the 'help' command
    HelpReply = f'This is a list of some of the phrases that I respond to. ' \
               f'I do not care about capitalization\n'

    # Append the list of simple text replies into the reply
    for key in Replies:        HelpList = HelpList + f'- {key}\n'

    # Now append the more complex commands
    HelpReply = HelpReply + "I can also respond to the following commands:\n"
    for command in bot.commands:        HelpReply += f"- {command}\n"

    # The reply is fully assembled, time to send it to the channel
    await ctx.send(HelpReply)

    return

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Did you call my name? Type 'Moji, help' for a list of actions that i can perform!")

@bot.event
async def scream(ctx):
    X = True;
    if X:
        await ctx.channel.send(f'Sorry, I cannot scream until master fixes the path of the audio files')
        return         # This function is temporally disabled till it can be properly migrated to the server

    if ctx.author.voice:    # This line checks if the user is in a voice channel
        channel = ctx.author.voice.channel
        # They are indeed in a channel, so first, answer the petition
        await ctx.channel.send(f'Okie doki pokie!')
        await asyncio.sleep(1)
        # Now, lets connect to their channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('AudioFiles/scream.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(5)      # Dont disconnect until the audio finishes playing
        await vc.disconnect()       # We finished our business, time to leave.

        # player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
        # player.start()
        # while not player.is_done():
        #    await asyncio.sleep(1)
        # disconnect after the player has finished
        # player.stop()
        # await vc.disconnect()
    else:
        await ctx.channel.send(f'I dont see you in any voice channel')

@bot.event
async def sing(ctx):
    X = True;
    if X:
        await ctx.channel.send(f'Sorry, I cannot scream until master fixes the path of the audio files')
        return  # This function is temporally disabled till it can be properly migrated to the server
    if ctx.author.voice:  # This line checks if the user is in a voice channel
        # They are indeed in a channel, so first, answer the petition
        channel = ctx.author.voice.channel
        await ctx.channel.send(f'Okie doki pokie!')
        await asyncio.sleep(1)
        # Now, lets connect to their channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio('AudioFiles/IsabelleSong.mp3'), after=lambda e: print('done', e))
        await asyncio.sleep(194)
        await vc.disconnect()

                # player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
                # player.start()
                # while not player.is_done():
                #    await asyncio.sleep(1)
                # disconnect after the player has finished
                # player.stop()
                # await vc.disconnect()
    else:
        await ctx.channel.send(f'I dont see you in any voice channel')

@bot.event
async def rock(ctx):
    if f'{ctx.author}' == 'anthonyzf20':    await ctx.channel.send('Paper! I win!')
    else:                                   await ctx.channel.send( RockPaperScissors('rock'))
@bot.event
async def paper(ctx):
    if f'{ctx.author}' == 'anthonyzf20':    await ctx.channel.send('Scissors! I win!')
    else:                                   await ctx.channel.send( RockPaperScissors('paper'))
@bot.event
async def scissors(ctx):
    if f'{ctx.author}' == 'anthonyzf20':    await ctx.channel.send('Rock! I win!')
    else:                                   await ctx.channel.send( RockPaperScissors('scissors'))

bot.run(os.environ['BotToken']) # Bot's unique token, stored in the .env file within the same directory as the rest of the project
