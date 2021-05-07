import requests
import json
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord_slash import SlashCommand , SlashCommandOptionType , SlashContext

load_dotenv()
giphy = os.environ.get('GIPHY_API')
discordToken = os.environ.get('DISCORD_TOKEN')

url = "http://api.giphy.com/v1/gifs/random"
params = {
    "tag": "swear trek",
    "api_key": giphy,
    "limit": "1"
    }

client = commands.Bot(command_prefix='!')
slash = SlashCommand(client , sync_commands=True)

@client.event
async def on_ready():
    print("Bot is logged in as {0.user}".format(client))


@slash.slash(name = 'st', description="Return a random Swear Trek gif.")
async def st(ctx : SlashCommand ):
    r = requests.get(url, params)
    rJson = json.loads(r.text)
    embedUrl = (rJson['data']['images']['downsized']['url'])
    embed = discord.Embed(
        title="Swear Trek",
        color=discord.Colour.purple())
    embed.set_image(url=embedUrl)
    await ctx.send(embed=embed)

client.run(discordToken)

