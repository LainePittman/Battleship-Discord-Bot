import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def play(ctx):
    await ctx.send("Starting battleship game!")
    #Drawing the one of the boards
    board = [
        ['1', '2', '3', '4', '5'],
        ['6', '7', '8', '9', '10'],
        ['11', '12', '13', '14', '15'],
        ['16', '17', '18', '19', '20'],
        ['21', '22', '23', '24', '25']
    ]
    board_display = "\n".join([" ".join(row) for row in board])
    await ctx.send(f"Here is your board:\n```\n{board_display}\n```")


bot.run(token, log_handler=handler, log_level=logging.DEBUG)