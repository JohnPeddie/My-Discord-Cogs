import discord
from discord.ext import commands
from random import randint

class dice: #name of cog
    """a cog to roll a dice"""

    def __init__(self, bot):   #neccesarry to set up as a cog for flazbot
        self.bot = bot

    @commands.command()     #this goes before every command
    async def dice(self, x):  #command name and then its just like a normal python function
        """Usage: Dice x, rolls a dice with x many sides"""
        x=int(x)
        y = randint(1,x)
        
        await self.bot.say("The dice rolled: {}".format(y))  #how the bot outputs, its not like print, you have to use the .format, it replaces the {} with y

def setup(bot):
    bot.add_cog(dice(bot))
