import discord
from discord.ext import commands

marketcap = 20000
balance = 1000
shareprice =10
totalshares =2000
shares=0

class invest:
    """In theory this is an acurate stock sim"""

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def buy(self, ammount):
        """this is legit only to see if the thing works and doesnt do anything"""
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares           
        
        shares = shares+ammount
        marketcap += (shareprice*ammount)
        shareprice += (ammount/totalshares)*shareprice        
        
        
        await self.bot.say("you just purchased {} shares".format(ammount))
        
    @commands.command()
    async def sell(self, ammount): 
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares           
        
        shares = shares+ammount
        marketcap += (shareprice*ammount)
        shareprice += (ammount/totalshares)*shareprice         
        
        
        await self.bot.say("you just sold {} shares".format(ammount))
        
    @commands.command()
    async def stats(self): 
        global shareprice
        
        await self.bot.say("shareprice = {}".format(shareprice))    

def setup(bot):
    bot.add_cog(invest(bot))
