import discord
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=commands.when_mentioned, intents=intents, application_id='1200413196293521499')

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(f'Message from {message.author} on {message.channel}: {message.content}')

@bot.command()
async def sync(ctx) -> None:
    fmt = await ctx.bot.tree.sync(guild=ctx.guild)
    await ctx.send(f'Synced {len(fmt)} commands.')
    
async def load():
    for file in os.listdir('./cogs'):
        if file.endswith('.py'):
            await bot.load_extension(f'cogs.{file[:-3]}')

async def main():
    await load()
    await bot.start(str(os.getenv('TOKEN')))
    
asyncio.run(main())