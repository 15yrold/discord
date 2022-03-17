import discord
import requests
from discord.ext import commands

token = input(f'Token Here => ')
prefix = input(f'Enter Prefix => ')
headers = headers = {'Authorization': f'Bot {token}'}
intents = discord.Intents(messages = True, guilds = True, members = True)
client = commands.Bot(
    description = "",
    self_bot = False,
    command_prefix = prefix,
    case_insensitive = True,
    guild_subscriptions = True, 
    intents = intents
)

@client.command()
async def fetch_user(ctx, user: discord.User = None):
    r = requests.get(f'https://discord.com/api/users/{user.id}', headers = headers).json()
    print(r)
    bannerurl = str(r['banner'])
    em = discord.Embed(description = f'{user}\'s Banner')
    em.set_image(url = f'https://cdn.discordapp.com/banners/{user.id}/{bannerurl}?size=1024')
    await ctx.send(embed = em)
    
client.run(token)
