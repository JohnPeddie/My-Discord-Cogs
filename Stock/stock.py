# Standard Library
import asyncio
import os
import random
import shutil
import uuid
from copy import deepcopy
from datetime import datetime

# Discord / Red
import discord
from discord.ext import commands
#from .utils import checks
#from .utils.dataIO import dataIO
#from __main__ import send_cmd_help


marketcap = 20000
balance = 1000
shareprice =10
totalshares =2000
shares=0

class stock:
    """Does some funky stock market shit"""
    
    def __init__(self, bot):
        self.bot = bot
    

    @stock.command(name="buy", pass_context=True)
    async def buy(amount):
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares    
        
        self.subtract_costs(shareprice*amount)
        #balance = balance -(shareprice*amount)
        shares = shares+amount
        marketcap += (shareprice*amount)
        shareprice += (amount/totalshares)*shareprice
    @stock.command(name="sell", pass_context=True)
    async def sell(amount):
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares 
        self.award_credits(shareprice*amount)
        #balance = balance +(shareprice*amount)
        shares = shares-amount
        marketcap -= (shareprice*amount)
        shareprice -= (amount/totalshares)*shareprice    
    @stock.command(name="stats", pass_context=True)
    def stats():
        print ("The share price is", shareprice)
        print ("your balance is", balance)
        
    def award_credits(self, deposits):
        for player in deposits:
            bank = self.bot.get_cog('Economy').bank
            bank.deposit_credits(player[0], player[1])
        
    def subtract_costs(self, author, cost):
        bank = self.bot.get_cog('Economy').bank
        bank.withdraw_credits(author, cost)    


def main():

    ans = input("what would you like to do?, buy, sell, exit? ")

    while (ans !="exit"):
        if ans == "buy":
            amm = int(input("How many "))
            buy(amm)
            stats()
        if ans == "sell" :
            amm = int(input("How many "))
            sell(amm)
            stats()
                
        ans = input("what would you like to do?, buy, sell, exit? ")


    
main()    
def setup(bot):
    bot.add_cog(stock(bot))
