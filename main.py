import discord
from discord.ext import commands
from discord.ext.commands import cog
from discord.flags import Intents
import bot
from dotenv import load_dotenv


cogs = [bot]

apikey = os.getenv("API_KEY")    
client = commands.Bot(command_prefix=';', Intents= discord.Intents.all)

for i in range(len(cogs)):
    cogs[i].setup(client)

print("BOT STARTED")

client.run(apikey)

