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
        self.file_path = "data/stock/stock.json"
        self.system = dataIO.load_json(self.file_path)
        self.version = "3.0.06"
    

    @stock.command(name="buy", pass_context=True)
    async def buy(amount):
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares    

        balance = balance -(shareprice*amount)
        shares = shares+amount
        marketcap += (shareprice*amount)
        shareprice += (amount/totalshares)*shareprice
    @stock.command(name="sell", pass_context=True)
    def sell(amount):
        global marketcap
        global balance
        global shares
        global shareprice
        global totalshares 
    
        balance = balance +(shareprice*amount)
        shares = shares-amount
        marketcap -= (shareprice*amount)
        shareprice -= (amount/totalshares)*shareprice    
    @stock.command(name="stats", pass_context=True)
    def stats():
        print ("The share price is", shareprice)
        print ("your balance is", balance)
    


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