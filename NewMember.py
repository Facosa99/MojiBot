async def AutomaticWelcome(member, client):
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