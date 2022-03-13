import os
import fade
import discord
import requests
from colorama import Fore
#from notifypy import Notify
from discord.ext import commands

r = f'{Fore.RED}'
b = f'{Fore.BLUE}'
y = f'{Fore.YELLOW}'
g = f'{Fore.GREEN}'
w = f'{Fore.WHITE}'
m = f'{Fore.MAGENTA}'
lightred = f'{Fore.LIGHTRED_EX}'
lightblue = f'{Fore.LIGHTBLUE_EX}'
lightyellow = f'{Fore.LIGHTYELLOW_EX}'
lightblack = f'{Fore.LIGHTBLACK_EX}'
lightgreen = f'{Fore.LIGHTGREEN_EX}'
lightmagenta = f'{Fore.LIGHTMAGENTA_EX}'

def cls():
    os.system('cls')
def size():
    os.system('mode 58,20')

cls()
token = input(f'{lightblack}> {lightblue}Discord Token {lightblack}-> {lightblue}')
cls()
prefix = input(f'{lightblack}> {lightblue}Command Prefix {lightblack}-> {lightblue}')
celia = commands.Bot(command_prefix = prefix, case_insensitive = True, self_bot = True)
celia.remove_command('help')
cstatus = ''
color = 0xB29FFF

link = f'https://canary.discordapp.com/api/v9/users/@me/settings'
headers = {
    'authorization': token,
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
    'content-type': 'application/json'
}
#notify = 'notification'

#def notify():
#    notify = Notify()
#    notify.title = f'Status Changed!'
#    notify.message = f'Status Changed to {cstatus}'
#    notify.icon = f'./status.ico'
#    notify.application_name = f'Discord Status Changer.'
#    notify.send()

@celia.event
async def on_ready():
    size()
    cls()
    maintext = f'''
             ██╗██████╗ ██████╗ ██╗  ██╗
            ███║╚════██╗╚════██╗██║  ██║
            ╚██║ █████╔╝ █████╔╝███████║
             ██║██╔═══╝ ██╔═══╝ ╚════██║
             ██║███████╗███████╗     ██║
             ╚═╝╚══════╝╚══════╝     ╚═╝         
                    By: liar#1224  
                    
Current User -> {celia.user}
Current Prefix -> {prefix}  
'''
    text = fade.purplepink(maintext)
    print(text)

@celia.command()
async def online(ctx):
    global cstatus
    await ctx.message.delete()
    try:
        status = {
            'status': 'online'
        }
        requests.patch(link, headers = headers, json = status)
        cstatus = f'Online'
        print(f'{g}Changed Status to -> {lightgreen}Online')
        #notify()
    except:
        print(f'{r}Couldnt Change Status to -> {lightgreen}Online')
        pass

@celia.command()
async def idle(ctx):
    global cstatus
    await ctx.message.delete()
    try:
        status = {
            'status': 'idle'
        }
        requests.patch(link, headers = headers, json = status)
        cstatus = f'Idle'
        print(f'{y}Changed Status to -> {lightyellow}Idle')
        #notify()
    except:
        print(f'{r}Couldnt Change Status to -> {lightyellow}Idle')
        pass

@celia.command()
async def dnd(ctx):
    global cstatus
    await ctx.message.delete()
    try:
        status = {
            'status': 'dnd'
        }
        requests.patch(link, headers = headers, json = status)
        cstatus = f'Do Not Disturb'
        print(f'{r}Changed Status to -> {lightred}Do Not Disturb')
        #notify()
    except:
        print(f'{r}Couldnt Change Status to -> {lightred}Do Not Disturb')
        pass

@celia.command(aliases = ['offline'])
async def invisible(ctx):
    global cstatus
    await ctx.message.delete()
    try:
        status = {
            'status': 'invisible'
        }
        requests.patch(link, headers = headers, json = status)
        cstatus = f'Invisible'
        print(f'{lightblack}Changed Status to -> {w}Offline')
        #notify()
    except:
        print(f'{r}Couldnt Change Status to -> {lightblack}Offline')
        pass

@celia.command()
async def help(ctx):
    await ctx.message.delete()
    em = discord.Embed(description = f'''``• Help - Shows this
• Online - Changes status to Online
• Idle - Changes sttaus to Idle
• Do Not Disturb - Changes status to Do Not Disturb
• Invisible - Changes status to Invisible``''', color = color)
    em.set_author(name = f'Status Tool', icon_url = f'{ctx.author.avatar_url}')
    em.set_footer(text = f'Made By: liar#1224', icon_url = f'{ctx.author.avatar_url}')
    em.set_thumbnail(url = f'{ctx.author.avatar_url}')
    await ctx.send(embed = em, delete_after = 3)

@celia.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.message.delete()

celia.run(token, bot = False)
