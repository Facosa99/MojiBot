import asyncio
import discord                          # Documentation: https://discordpy.readthedocs.io/en/stable/index.html
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from NewMessage import Responses
from NewMember import AutomaticWelcome

load_dotenv()                           # Refresh enviroment

# intents are the permissions for the bot
intents = discord.Intents.default()
intents.members = True                  # Detect events related to a server member. For example, a new arrival or someone leaving the server
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)  # After setting the right permissions, send them

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
        await message.channel.send('"bot.tree.sync()" is temporaily disabled, masterr')
        return

    if message.author == bot.user: return   # if current message is from Bot itself, ignore it and finish the function.
                                            # This prevents the bot from replying to itself and thus avoids undesirable loops.

    await bot.process_commands(message)     # Check if received message is a command before trying regular replies
    await Responses(message, bot)           # Now try regular replies
    return


# -------------------------------------List of all available commands---------------------------------------------------
@bot.command(name='say')
async def say(ctx, *arg):
    Text = " ".join(arg)
    await ctx.send(f"{Text}")
    await ctx.message.delete()
    return

@bot.command(name='list', help="Gotta get this shit running")
async def list(ctx):
    await ctx.send(f"Here is the list of all available commands:\n"
                   f"- (Insert list here)")
    return

#@bot.command(name="test_1", )

bot.run(os.environ['BotToken']) # Bot's unique token, stored in the .env file within the same directory as the rest of the project