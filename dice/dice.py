import discord
from discord.ext import commands
from random import randint

class dice:
    """a cog to roll a dice"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def dice(self, x):
        """Usage: Dice x, rolls a dice with x many sides"""
        x=int(x)
        y = randint(1,x)
        
        await self.bot.say("The dice rolled: {}".format(y))

def setup(bot):
    bot.add_cog(dice(bot))
