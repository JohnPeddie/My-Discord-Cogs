import discord
from discord.ext import commands
from .utils import checks
from cogs.utils.chat_formatting import pagify, box


johnid = "186439054139588608"
aqeelid = "186447263558533120"
adamid = "186449433209077760"
adambalance = [0,0,int(adamid)]
aqeelbalance = [0,0,int(aqeelid)]
johnbalance = [0,0,int(johnid)]

def idtoname(name): #a random function to turn Ids to names until I work out how to do it in discord
    name = str(name)
    if name == "186439054139588608":
        return ("John")
    if name == "186449433209077760":
        return ("Adam") 
    if name == "186447263558533120":
        return ("Aqeel")        

class McFlurryBucks:
    """Cog for keeping track of McB ballances"""
    
    def __init__(self, bot):
        self.bot = bot  
        
    
    
        
    @commands.command(pass_context=True)
    async def balance(self, ctx, user: discord.Member=None):
        """Gets the balance of a user, defaults to you, you can also check others"""
        global adambalance
        global aqeelbalance
        global johnbalance
        global johnid
        global aqeelid
        global adamid
        author = ctx.message.author
        x= author.id # This is your author id number
        
        z= author.name # This is the author's id
        
        if not user:
            
        
            if x == johnid :
                total = johnbalance[0]+johnbalance[1]
                aqeel = johnbalance[0]
                adam = johnbalance[1]
                await self.bot.say("Your balance is {}McB, owed {}McB by Aqeel and {}McB by Adam".format(total,aqeel,adam))
            
            if x == adamid:
                total = adambalance[0]+adambalance[1]
                aqeel = adambalance[0]
                john = adambalance[1]
                await self.bot.say("Your balance is {}McB, owed {}McB by Aqeel and {}McB by John".format(total,aqeel,john))  
            
            if x == aqeelid:
                total = aqeelbalance[0]+aqeelbalance[1]
                john = aqeelbalance[0]
                adam = aqeelbalance[1]
                await self.bot.say("Your balance is {}McB, owed {}McB by John and {}McB by Adam".format(total,john,adam))
        else: 
            y= user.id # This is the user's id
            a= user.name # This is the user's name 
            if y != x:
                if y == johnid:
                    total = johnbalance[0]+johnbalance[1]
                    aqeel = johnbalance[0]
                    adam = johnbalance[1]
                    await self.bot.say("{}'s balance is {}McB, owed {}McB by Aqeel and {}McB by Adam".format(a,total,aqeel,adam))
                
                if y == adamid:
                    total = adambalance[0]+adambalance[1]
                    aqeel = adambalance[0]
                    john = adambalance[1]
                    await self.bot.say("{}'s balance is {}McB, owed {}McB by Aqeel and {}McB by John".format(a,total,aqeel,john))  
                        
                if y == aqeelid:
                    total = aqeelbalance[0]+aqeelbalance[1]
                    john = aqeelbalance[0]
                    adam = aqeelbalance[1]
                    await self.bot.say("{}'s balance is {}McB, owed {}McB by John and {}McB by Adam".format(a,total,john,adam))             
            
        
    @commands.command(pass_context=True)
    async def pay(self, ctx, user: discord.Member, amount):
        global adambalance
        global aqeelbalance
        global johnbalance  
        global johnid
        global aqeelid
        global adamid         
        author = ctx.message.author
        x= author.id # This is your author id number
        y= user.id # This is the user's id
        z= author.name # This is the author's id
        a= user.name # This is the user's name
        amount = int(amount)
        q= 0
        if (amount <= 0):
            q= 1
            await self.bot.say("Your amount has to be greater than 0, you fool")
        elif (x==y):
            q=1
            await self.bot.say("You can't pay yourself, fool")         
        elif (q==0):
            if y== johnid:
                if x== adamid:
                    johnbalance[1]+= amount
                if x == aqeelid:
                    johnbalance[0]+= amount
            if y== adamid:
                if x== johnid:
                    adambalance[1]+= amount
                if x == aqeelid:
                    adambalance[0]+= amount   
            if y== aqeelid:
                if x== adamid:
                    aqeelbalance[1]+= amount
                if x == johnid:
                    aqeelbalance[0]+= amount        
            await self.bot.say("Amount of {}McB successfully paid!".format(amount))
                
              
       
            
        
    
    @commands.command()
    @checks.admin_or_permissions(manage_server=True)
    async def setbalance(self, user, a,b):
        """Sets balances of a user, admin reserved, users look like this: john[aqeel, adam], aqeel[john, adam], adam[aqeel, john]"""
        a= int(a)    
        b=int(b)
        if user == "adam":
            adambalance = [a,b]
        if user == "john":
            johnbalance = [a,b] 
        if user == "aqeel":
            aqeelbalance = [a,b]  
            
    @commands.command()
    async def balances(self): #after here is where I put the id in the account list, so things might get weird, I should probably rewrite all the code above, but meh
        global adambalance
        global aqeelbalance
        global johnbalance  
        global johnid
        global aqeelid
        global adamid 
        
        scores = [[aqeelbalance[0]+aqeelbalance[1],aqeelbalance[2]],[johnbalance[0]+johnbalance[1],johnbalance[2]],[adambalance[0]+adambalance[1],adambalance[2]]]
        highscore="Balances of the users: \n\n"
        
        for x in scores:
            highscore += idtoname(x[1])+ (8-(len(idtoname(x[1]))-4))*" "+str(x[0])+"McB \n"
        
        for page in pagify(highscore, shorten_by=12):
            await self.bot.say(box(page, lang="py"))        
    
        
        
    
            
        

def setup(bot):
    bot.add_cog(McFlurryBucks(bot))
