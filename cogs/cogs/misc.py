#importing libraries
import discord
from discord.ext import commands
import random
from googleapiclient.discovery import build
import config


class misc(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("misc.py is online")


    @commands.command()
    async def imagesearch(self, ctx,* ,search):
        ran = random.randint(0,9)
        resource = build("customsearch", "v1", developerKey = config.GOOGLE_API_KEY).cse()
        result = resource.list(
            q=f"{search}", cx = "799a59d61296713c8", searchType = "image"
        ).execute()
        url = result["items"][ran]["link"]
        imageEmbed = discord.Embed(title = f"Result for {search.title()}")
        imageEmbed.set_image(url = url)
        await ctx.send(embed = imageEmbed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'''Pong! 
Server responded in {round(self.client.latency * 1000)}ms''')

    @commands.command()
    async def diceroll(self, ctx, sides = 6):
        if sides == None:
            sides == 6
        else:
            sides == sides
        roll = random.randint(1,sides)
        await ctx.send(roll)

    @commands.command()
    async def pfp(self, ctx, *, member: discord.Member):

        colour = discord.Color.blue()
        if not member:
            member == ctx.author
        else:
            member == member
        embed = discord.Embed(title=f"{member}'s Profile Picture", color= colour)
        embed.set_image(url=member.avatar.url)
        await ctx.send(embed=embed)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        color = discord.Color.blue()
        avatar = member.avatar.url
        userInfo_Embed = discord.Embed(colour=color, timestamp=ctx.message.created_at)
        userInfo_Embed.set_author(name=f"Info about {member}")
        userInfo_Embed.set_thumbnail(url=avatar)
        userInfo_Embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        userInfo_Embed.add_field(name="Username", value=member.name, inline=True)
        userInfo_Embed.add_field(name="Discriminator", value=member.discriminator, inline=True)
        userInfo_Embed.add_field(name="Bot?", value=member.bot, inline=True)
        userInfo_Embed.add_field(name="Joined Server", value=member.joined_at.date(), inline=True)
        userInfo_Embed.add_field(name="Account Created", value=member.created_at.date(), inline=True)
        userInfo_Embed.add_field(name="Status", value=member.status, inline=True)
        await ctx.send(embed=userInfo_Embed)

async def setup(client):
    await client.add_cog(misc(client))