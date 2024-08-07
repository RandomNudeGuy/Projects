# bot.py

import discord
from discord.ext import commands
from BMI Calc import calculate_bmi  # Import the BMI calculator function

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"Yoo, I'm {bot.user.name}, and I'm ready!")

@bot.command()
async def bmi(ctx, weight: float, height: float):
    result = calculate_bmi(weight, height)
    await ctx.send(f"Hey {ctx.author.mention}, {result}")

bot.run('MTI2MzIxODgxNzgyNDMyNTc4Mw.GOF0zJ.5zI-1vm_E52PR1oLNSbew5xWhusEsJOeVwaceI')




# import discord
# from discord.ext import commands,tasks 


# intents = discord.Intents.all()
# bot = commands.Bot(command_prefix='?', intents = intents,help_command = None)

# def calc():
    
# @bot.event
# async def on_ready():
#     print(f"Yoo, im {bot.user.name}, and im ready!")

# @bot.command()
# async def hi(ctx, num1: float, num2: float):
#     await ctx.send(f"""Hey {ctx.author.mention}, 
# here is your numbers: {num1}, {num2}""")
    

# # @bot.command(name='שלום')
# # async def hi(ctx):
# #     await ctx.send("YOOO")

# bot.run('MTI2MzIxODgxNzgyNDMyNTc4Mw.GOF0zJ.5zI-1vm_E52PR1oLNSbew5xWhusEsJOeVwaceI')


