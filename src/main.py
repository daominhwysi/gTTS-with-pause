import discord
from discord import app_commands
from dotenv import load_dotenv
import os
from function.f88 import gttsp
load_dotenv()
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@tree.command(name='ttswp',description='send Text to speech file but with custom pause time')
async def ttswp(interaction: discord.Interaction,content : str,number :int):
    await interaction.response.defer()
    op = gttsp(content,number)
    if op[0] == True:
     await interaction.followup.send(file=discord.File(fr'{op[1]}'))
    elif op[0] == False:
       ttswp()
@client.event
async def on_ready():
    await tree.sync()
    print("Ready!")

client.run(os.getenv('TOKEN'))