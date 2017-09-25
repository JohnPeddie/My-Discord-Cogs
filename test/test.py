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
        await self.bot.say("I am a massive dn but I think this works")

def setup(bot):
    bot.add_cog(test(bot))
