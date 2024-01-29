import discord
import os
from dotenv import load_dotenv

load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        
    async def on_message(self, message):
        print(f'Message from {message.author} on {message.channel}: {message.content}')
        
intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(str(os.getenv("TOKEN")))