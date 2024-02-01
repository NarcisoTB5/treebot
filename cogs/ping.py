import discord
from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Ping cog loaded.')
                
    @app_commands.command(name='ping', description=' A simple ping command!')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message('Pong!')
        
async def setup(bot):
    await bot.add_cog(Ping(bot), guilds=[discord.Object(id=1155956471645864008)])