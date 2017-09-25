import discord
from discord.ext import commands

class test:
    """first test"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self):
        """idk lol!"""

        #Your code will go here
        await self.bot.say("I can do stuff!")

def setup(bot):
    bot.add_cog(Mycog(bot))
