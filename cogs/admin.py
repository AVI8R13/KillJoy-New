import discord
from discord import activity, FFmpegPCMAudio, Member, app_commands
from discord.ext import commands
from datetime import datetime, timedelta

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        print("admin.py is online!")


    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    async def setnick(self, ctx , member: discord.Member, *, nick):
        await member.edit(nick=nick)
        await ctx.send(f"Nickname was changed for @{member}")

async def setup(client):
    await client.add_cog(admin(client))