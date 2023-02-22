
from discord import app_commands
import discord
from discord.ext import commands
import openai
import aiohttp
import config

class openAi(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("misc.py is online")


    @commands.command()
    async def dalle(ctx, *, UserPrompt):
        await ctx.send('Image is generating..')
        response = openai.Image.create(prompt = UserPrompt, size="1024x1024")
        image_url = response['data'][0]['url']
        color = discord.Color.blue()
        dalleEmbed = discord.Embed(title = '''Dalle's Image''', color = color)
        dalleEmbed.set_image(url = image_url)
        await ctx.send(embed = dalleEmbed)
                

async def setup(client):
    await client.add_cog(openAi(client))