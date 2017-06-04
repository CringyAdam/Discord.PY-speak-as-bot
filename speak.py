#         © Copyright Adam Aharony (a.k.a. Cringy Adam)
#                    All rights reserved
#      Twitter: @AdamAharony, Discord: @Cringy Adam#4611


import discord
import asyncio
import sys
import config

client = discord.Client()
channelid = config.channelid
token = config.token
botstatus = config.isBot

if botstatus == 'yes':
    botstatus = True
elif botstatus == 'no':
    botstatus = False


@client.event
async def on_ready():
    print(f'> Logged in as: {client.user}')
    print(client.user.id)
    print('-----READY----- \n')
    await console_input()
    

@client.event
async def console_input():
    await client.wait_until_ready()
    msg = input('> Message to send: ')
    await client.send_message(discord.Object(id=channelid), msg)
    print('')
    await console_input()


client.run(token, bot=botstatus)
