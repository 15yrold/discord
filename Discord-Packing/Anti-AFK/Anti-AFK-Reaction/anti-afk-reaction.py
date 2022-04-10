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
emojis = open('emojis.txt')
client = discord.Client()

@client.event
async def on_ready():
    log('{}'. format(client.user))

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        for emoji in emojis:
            await message.add_reaction(emoji)
            log('Sent -> {}'.format(emoji))

client.run(token, bot = False)
