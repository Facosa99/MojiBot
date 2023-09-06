import asyncio
import discord                          # Documentation: https://discordpy.readthedocs.io/en/stable/index.html
import os
from dotenv import load_dotenv
from NewMessage import Responses
from NewMember import AutomaticWelcome
load_dotenv()                           # Refresh enviroment

# intents are the permissions for the bot
intents = discord.Intents.default()
intents.members = True                  # Detect events related to a server member. For example, a new arrival or someone leaving the server
intents.message_content = True
client=discord.Client(intents=intents)  # After setting the right permissions, send them

@client.event       # This code block is executed once, after the Bot logins
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event       # This code block is executed everytime a new member joins the server
async def on_member_join(member):
    await AutomaticWelcome(member, client)

@client.event       # This code block is executed everytime a new message is detected
async def on_message(message):
    await Responses(message, client)

client.run(os.environ['BotToken']) # Bot's unique token, stored in the .env file within the same directory as the rest of the project