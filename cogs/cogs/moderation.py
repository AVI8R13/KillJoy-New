import discord
from discord import activity, FFmpegPCMAudio, Member, app_commands, SelectOption, permissions
from discord.ext import commands
from datetime import datetime, timedelta


class moderation(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("moderation.py is online!")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason="none"):
        await member.kick(reason=reason)
        responsible = ctx.author
        timedate = datetime.now()
        embed = discord.Embed(title= f'{member} has been kicked!', color = discord.Color.red())
        embed.add_field(name = 'Reason: ',value = reason, inline = False)
        embed.add_field(name = 'Responsible moderator: ', value = responsible, inline= False)
        embed.add_field(name = 'Date: ', value = timedate , inline = False)
        await member.send(embed = embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason = "None"):
        await member.ban(reason=reason)
        responsible = ctx.author
        timedate = datetime.now()
        embed = discord.Embed(title= f'{member} has been banned!', color = discord.Color.red())
        embed.add_field(name = 'Reason: ',value = reason, inline = False)
        embed.add_field(name = 'Responsible moderator: ', value = responsible, inline= False)
        embed.add_field(name = 'Date: ', value = timedate , inline = False)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(mute_members=True)
    async def warn(self, ctx, member: discord.Member, *, reason = "None"):
        responsible = ctx.author
        timedate = datetime.now()
        embed = discord.Embed(title= f'{member} has been warned!', color = discord.Color.orange())
        embed.add_field(name = 'Reason: ',value = reason, inline = False)
        embed.add_field(name = 'Responsible moderator: ', value = responsible, inline=False)
        embed.add_field(name = 'Date: ', value = timedate , inline = False)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(manage_messages = True)
    async def purge(self, ctx, amount = 5):
        responsible = ctx.author
        timedate = datetime.now()
        await ctx.channel.purge(limit = amount)
        embed = discord.Embed(title = f'{amount} messages have been deleted!', color = discord.Color.blue())
        embed.add_field(name = 'Responsible moderator: ', value = responsible, inline = False)
        embed.add_field(name = 'Date: ', value = timedate , inline = False)
        await ctx.send(embed = embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def activity(self, ctx, *, activity):
        await self.client.change_presence(activity=discord.Game(activity))
        await ctx.send(f"Activity changed to {activity}!")

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def lockdown(self, ctx, *, reason = "None"):
        responsible = ctx.author
        timedate = datetime.now()
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=False)
        embed = discord.Embed(title=f"{ctx.channel.mention} is in lockdown!", color = discord.Color.red())
        embed.add_field(name = 'Reason: ',value = reason, inline = False)
        embed.add_field(name = 'Responsible moderator: ', value = responsible, inline= False)
        embed.add_field(name = 'Date: ', value = timedate , inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unlock(self, ctx):
        responsible = ctx.author
        timedate = datetime.now()
        await ctx.channel.set_permissions(ctx.guild.default_role,send_messages=True)
        embed = discord.Embed(title=f"{ctx.channel.mention} has been unlocked!", color=discord.Color.green())
        embed.add_field(name = 'Responsible moderator: ', value = responsible, inline= False)
        embed.add_field(name = 'Date: ', value = timedate , inline = False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(moderation(client))