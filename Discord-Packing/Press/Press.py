import os
import discord
import logging
from colorama import Fore

logging.basicConfig(
    level = logging.INFO,
    format = f'{Fore.LIGHTBLUE_EX}[{Fore.RESET}%(asctime)s{Fore.LIGHTBLUE_EX}] {Fore.RESET}%(message)s',
    datefmt = '%H:%M:%S'
)
log = logging.info
os.system('cls')
token = input(f'-> Token -> ')
client = discord.Client()
words = open('words.txt')

@client.event
async def on_ready():
    os.system('cls')
    log('{}'.format(client.user))

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):
        for word in words:
            await message.channel.send(word)
            log('Sent -> {}'.format(word))

client.run(token, bot = False)
