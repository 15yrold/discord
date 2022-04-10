import os
import logging
import discord
from colorama import Fore

logging.basicConfig(
    level = logging.INFO,
    format = f'{Fore.LIGHTBLUE_EX}[{Fore.RESET}%(asctime)s{Fore.LIGHTBLUE_EX}] {Fore.RESET}%(message)s',
    datefmt = '%H:%M:%S'
)
log = logging.info
os.system('cls')
token = input('Token: ')
client = discord.Client()

@client.event
async def on_ready():
    log('{}'. format(client.user))

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        await message.add_reaction('😎')
        log('Reacted to Ping!')

client.run(token, bot = False)
