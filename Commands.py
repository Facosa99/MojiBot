import random
import json
import asyncio

import discord
from rule34Py import rule34Py


async def RockPaperScissors (ctx, Attack):
    Defense = random.randint(0, 2)
    MojiWins = {"rock": "Paper", "paper":"scissors", "scissors":"rock"}
    MojiTies = {"rock": "Rock", "paper": "Paper", "scissors": "Scissors"}
    MojiLoses = {"rock": "Scissors", "paper": "Rock", "scissors": "Paper"}

    if   Defense == 0 or f'{ctx.author}' == 'anthonyzf20':    # User anthonyzf20 will always lose, personal reasons
            await ctx.channel.send(f'I choose {MojiWins[Attack]}! I Win!')
            return
    elif Defense == 1:
            await ctx.channel.send(f'I choose {MojiTies[Attack]}! huh, a tie')
            return
    else:
            await ctx.channel.send(f'I choose {MojiLoses[Attack]}! Aw, I lose!')
            return

async def Say(ctx, *arg):
    await ctx.send(" ".join(arg))   # Print as String rather than tuple, to avoid this: ("dictionary", "format")
    await ctx.message.delete()
    del(arg)
    return

async def HelpReply(ctx, current_dir, bot):
    HelpReply = f''


    # The following code is required only when JSON replies are enabled
    # Open the JSON file with the list of simple text replies
    with open(current_dir + '/QuickResponses.json', 'r') as openfile:
        ResponsesList = json.load(openfile)

    Replies = ResponsesList  # Dump the info of said file into a dictionary
    # Create a String to store our reply to the 'help' command
    HelpReply = f'This is a list of some of the phrases that I respond to. ' \
                f'I do not care about capitalization\n'
    # Append the list of simple text replies into the reply
    for key in Replies:        HelpReply = HelpReply + f'- {key}\n'

    # Now append the more complex commands

    HelpReply = HelpReply + "\nI can also respond to the following commands:\n"
    for command in bot.commands:        HelpReply += f"- {command}\n"

    # The reply is fully assembled, time to send it to the channel
    await ctx.send(HelpReply)
    return

async def PlayAudio(ctx, current_dir, filename):
    # First we gotta check if the invoker is currently in an audio channel
    if ctx.author.voice:    # In case the user is indeed in a voicechat
        channel = ctx.author.voice.channel
        # They are indeed in a channel, so first, answer the petition
        await ctx.channel.send(f'Okie doki pokie!')
        await asyncio.sleep(1)
        # Now, lets connect to their channel
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(f'{current_dir}/AudioFiles/{filename}'), after=lambda e: print('done', e))
        await asyncio.sleep(5)      # Dont disconnect until the audio finishes playing
        await vc.disconnect()       # We finished our business, time to leave.

        # player = vc.create_ffmpeg_player('scream.mp3', after=lambda: print('done'))
        # player.start()
        # while not player.is_done():
        #    await asyncio.sleep(1)
        # disconnect after the player has finished
        # player.stop()
        # await vc.disconnect()
    else:               # In case the user is not in a voicechat
        await ctx.channel.send(f'I dont see you in any voice channel')

async def Rule34(ctx, *Tags):
    r34Py = rule34Py()
    # print(r34Py.version)  # Powered by this wonderful repository: https://github.com/b3yc0d3/rule34Py

    if ctx.channel.is_nsfw() == False:
        await ctx.channel.send(f'Sorry, I can only do that in a lewd channel')
        return      # If the channel isnt NSFW, stop the function here.
    if len(Tags) == 0:
        await ctx.channel.send(f'Sorry, you did not specified any tags for the search. For more information, type'
                               f'"Moji, rule34 help"')

    if f'{Tags[0].lower()}' == 'help':       # Describe the command
        await ctx.channel.send(f'Hi :heart:, the "Rule34" command can be used in many different ways.\n'
                               f'- "Moji, rule34 <tags>" gives you a random image or video with the specified tag or tags\n'
                               f'- "Moji, rule34 search <tags>" shows you the 5 most recent pictures or video with the specified tags')
        return

    elif f'{Tags[0].lower()}' == 'search':   # If user specifies 'search', look for the first results for the specified Tags
        Tags = " ".join(Tags[1:]).lower()

        if len(Tags) == 0:
            await ctx.channel.send(f'Sorry, you did not specified any tags for the search. For more information, type'
                                   f'"Moji, rule34 help"')
            return      # If the user didnt specify any tags, stop the function here
        search = r34Py.search([Tags], limit=5)

        await ctx.channel.send(f'Okie dokie pokie! Im searching the firsts results for "{Tags}"')
        if search:
            results = f''
            for result in search:
                results = results + f'- {result.image}{result.video}\n'
            await ctx.channel.send(f"{results}")

        else:
            await ctx.channel.send(f"Sorry, I could not find any result")
        return

    elif    f'{Tags[0].lower()}' == 'top':   # If user specifies 'top', show today's favorites
        top = r34Py.top_favorites()
        await ctx.channel.send(f"Today's top favorites are {top}")

    else:                                    # Find a random artwork of the specified Tags
        await ctx.channel.send(f'Okie dokie pokie!, let me find something to your liking')
        Tags = " ".join(Tags).lower()

        result_random       = r34Py.random_post("")  # or r34Py.random_post()
        print(result_random)
        #result_tagmap       = r34Py.tagmap()

        #print(result_random.id)
        #print(result_random.image)
        if result_random:
            await ctx.channel.send(f'{result_random.image}{result_random.video}')
        else:
            await ctx.channel.send(f"I could not find any suitable result, sorry")
        del(Tags)
        return