import config
import discord 
from discord.ext import commands
from server import serverOnline
import os


def run():

    client = commands.Bot(intents=discord.Intents.all() , command_prefix= "." , description='.help')

    async def load():
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'cogs.{filename[:-3]}')

    @client.event
    async def on_ready():
        print(client.user)
        print(client.user.id)
        print("main.py is online")
        await load()

    client.run(config.TOKEN)

if __name__  == "__main__":
    run()




