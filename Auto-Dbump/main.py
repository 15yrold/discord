import discord
import time
import os

os = os.system

token = input(f'token -> ')
os('cls')
celia = discord.Client()

@celia.event
async def on_ready():
    print(f'hi {celia.user}')
    while True:
        channel = celia.get_channel('channel id here') # example: celia.get_channel(936931633091715112)
        time.sleep(7200)
        await channel.send('!d bump')

celia.run(token, bot = False)
