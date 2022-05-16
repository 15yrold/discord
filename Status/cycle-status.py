###################################################
#                                                 #
#                                                 #
# could get u disabled lol if delay time is super #
# low. Recommmended Time: 10-15 seconds           #
#                                                 #
#                                                 #
###################################################

import os
import time
import random
import requests
from discord.ext import commands

token = input('token: ')
client = commands.Bot(command_prefix = '>', self_bot = True)
headers = {
    'authorization': token,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
    'content-type': 'application/json'
}
api = 'https://canary.discordapp.com/api/v9/users/@me/settings'
codes = [200, 201, 204]
status_cycle = False

@client.event
async def on_ready():
    os.system('cls')
    print('ready')

@client.command(aliases = ['cs', 'statuscycle'])
async def cyclestatus(ctx, delay: int):
    global status_cycle
    status_cycle = True
    print('Status Cycle: {}\n Delay: {}'.format(status_cycle, delay))
    while status_cycle:
        time.sleep(int(delay))
        random_status = random.choice(['online', 'idle', 'dnd', 'invisible'])
        status = {
            'status': random_status
        }
        r = requests.patch(api, headers = headers, json = status)
        if r.status_code in codes:
            print('workedd')
        else:
            print('boneless pizza')

client.run(token, bot = False)
