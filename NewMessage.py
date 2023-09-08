import asyncio
import json
from pathlib import Path

import discord

# Current directory
current_dir = str(Path(__file__).resolve().parent).replace('\\', '/')

async def Responses(message):
        # if f'{message.author}' == 'anthonyzf20':  # Reply to this user everytime the bot detects a new message from then
        #   await message.channel.send('¿Quien?')  # Basically turn the bot into harasser-mode
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
        return                  # If we reach this far into the function, we haven't hit anything, close it.
