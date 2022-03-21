import discord
from discord.ext import commands
from discord_slash import SlashCommand

token = input(f'Enter Bot Token: ')
prefix = input(f'Enter Prefix: ')
intents = discord.Intents.all()
intents.members = True
intents = discord.Intents(messages = True, guilds = True, members = True)
client = commands.Bot(self_bot = False, command_prefix = '>', case_insensitive = True, guild_subscriptions = True,  intents = intents)
slash = SlashCommand(client, sync_commands = True)

# Normal Command
@client.command()
async def avatar(ctx, user: discord.User = None):
    if user == None:
        user = ctx.author
    em = discord.Embed(description = user.display_name + '\'s Profile Picture')
    em.set_image(url = user.avatar_url)
    em.set_footer(text = ' Requested By: {}'.format(ctx.author.display_name), icon_url = f'{ctx.author.avatar_url}')
    await ctx.send(embed = em)
    
# Slash Command
@slash.slash(name = f'Avatar', description = f'Displays user Profile Picture.', guild_ids = [guild_id]) # example: guild_ids = [952596515568889957]
async def avatar(ctx, user: discord.User = None):
    if user == None:
        user = ctx.author
    em = discord.Embed(description = user.display_name + '\'s Profile Picture')
    em.set_image(url = user.avatar_url)
    em.set_footer(text = 'Requested By: {}'.format(ctx.author.display_name), icon_url = f'{ctx.author.avatar_url}')
    await ctx.send(embed = em)
   
client.run(token)
