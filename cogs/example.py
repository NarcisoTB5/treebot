import discord
from discord import app_commands
from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        print('Example cog loaded.')
                
    @app_commands.command(name='example', description='This is an example command!')
    async def example(self, interaction: discord.Interaction):
        await interaction.response.send_message('It works!')
        
async def setup(bot):
    await bot.add_cog(Example(bot), guilds=[discord.Object(id=1155956471645864008)])