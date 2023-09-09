import asyncio
import discord                          # Documentation: https://discordpy.readthedocs.io/en/stable/index.html
import os
from dotenv import load_dotenv
from discord.ext import commands
from pathlib import Path

# Local Libraries
from NewMessage import Responses
from NewMember import AutomaticWelcome
from Commands import *

load_dotenv()                                                           # Refresh enviroment
current_dir = str(Path(__file__).resolve().parent).replace('\\', '/')   # Directory from which the program is executed/stored

# intents are the permissions for the bot
intents = discord.Intents.default()
intents.members = True                  # Detect events related to a server member. For example, a new arrival or someone leaving the server
intents.message_content = True          # Detects messages and their content, name is pretty self explanatory

bot = commands.Bot(command_prefix = ('Moji, ', 'moji, ', 'Moji ','Moji,', 'moji,', 'Moji'), intents=intents, help_command=None)  # Set the prefix and the permissions.

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

    # if current message is from Bot itself, ignore it and finish the function.
    # This prevents the bot from replying to itself and thus avoids undesirable loops.
    if message.author == bot.user: return

    # If you want simple responses to certain messages, set them in the associated JSON file and put this line. For more
    # interactive responses (like repeating the message text or doing an operation) use commands, as those can receive arguments
    if await Responses(message):
        return

    # Check if received message is a command. If your bot has no commands, then this line isnt necesary.
    # Also you might want to change from "bot" to "client". Setting it as "bot" is only necesary for enabling commands
    await bot.process_commands(message)


    # If the message mentioned moji but it wasnt detected as a Simple Response nor command, send default 'help' message
    content = f'{message.content.lower()}'
    if content==('moji') or content==('moji,') or content==('moji, '):
        await message.channel.send("Did you call my name? Type 'Moji, help' for a list of actions that i can perform!")
        return

#------------------------------------------------COMMANDS---------------------------------------------------
@bot.command(name='say', help="Makes Moji say whatever you want")
async def say(ctx, *phrase):
    await Say(ctx, *phrase)
    return

@bot.command(name='help', help="List all available interactions")
async def help(ctx):
    await HelpReply(ctx, current_dir, bot)
    return

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound): await ctx.send("Did you call my name? Type 'Moji, help' for a list of actions that i can perform!");
    return
@bot.command(name='scream', help="Gotta get this shit running")
async def scream(ctx):
    # This function is temporally disabled till it can be properly migrated to the server
    if True:        await ctx.channel.send(f'Sorry, I cannot scream until master fixes the path of the audio files')
    else:           await PlayAudio(ctx, current_dir, 'scream.mp3');    return
@bot.command(name='sing', help="Gotta get this shit running")
async def sing(ctx):
    # This function is temporally disabled till it can be properly migrated to the server
    if True:        await ctx.channel.send(f'Sorry, I cannot sing until master fixes the path of the audio files')
    else:           await PlayAudio(ctx, current_dir, 'IsabelleSong.mp3');  return
@bot.command(name='rock', help="Play 'Rock, Paper, Scissors' agaisnt Moji")
async def rock(ctx):
    await RockPaperScissors(ctx, "rock");       return
@bot.command(name='paper', help="Play 'Rock, Paper, Scissors' agaisnt Moji")
async def paper(ctx):
    await RockPaperScissors(ctx, "paper");      return
@bot.command(name='scissors', help="Play 'Rock, Paper, Scissors' agaisnt Moji")
async def scissors(ctx):
    await RockPaperScissors(ctx, "scissors");   return
@bot.command(name='rule34', help="testing rule34")
async def rule34(ctx, *Tags):
    await Rule34(ctx, *Tags);   return

bot.run(os.environ['BotToken']) # Bot's unique token, stored in the .env file within the same directory as the rest of the project
