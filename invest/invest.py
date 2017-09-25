import discord
from discord.ext import commands

class invest:
    """In theory this is an acurate stock sim"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def buy(self, ammount):
        """this is legit only to see if the thing works and doesnt do anything"""

        #Your code will go here
        await self.bot.say("you just baught{}".format(ammount))

def setup(bot):
    bot.add_cog(invest(bot))
