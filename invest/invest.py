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
        ammount = int(ammount)
        if (ammount < 1):
            await self.bot.say("You can only purchase one or more shares")        
        else:
            if ((balance - shareprice*ammount)>=0):
                balance -= shareprice*ammount
                shares = shares+ammount
                marketcap += (shareprice*ammount)
                shareprice += (ammount/totalshares)*shareprice        
        
            
                await self.bot.say("you just purchased {} shares".format(ammount))
            else:
                await self.bot.say("you cant afford that many shares") 
        
    @commands.command()
    async def sell(self, ammount): 
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares           
        ammount = int(ammount)
        if (ammount < 1):
            await self.bot.say("You can only sell one or more shares")
        else:  
            if (ammount > shares):
                await self.bot.say("You do not have that many shares to sell")
            else:
                balance += shareprice*ammount
                shares = shares-ammount
        
                marketcap -= (shareprice*ammount)
                shareprice -= (ammount/totalshares)*shareprice         
        
        
                await self.bot.say("you just sold {} shares".format(ammount))
        
    @commands.command()
    async def stats(self): 
        
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares          
        shareprice = round(shareprice, 3)
        await self.bot.say("shareprice = ${} per share".format(shareprice)) 
        await self.bot.say("market cap = ${}".format(marketcap))
        await self.bot.say("your balance = ${}".format(balance))
        await self.bot.say("you own = {} shares".format(shares))
        
        
    @commands.command()
    async def reset(self): 
        
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares 
        marketcap = 20000
        balance = 1000
        shareprice =10
        totalshares =2000
        shares=0        
        
        
        
def setup(bot):
    bot.add_cog(invest(bot))
