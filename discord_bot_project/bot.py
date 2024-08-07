# bot.py

import discord
import requests
from discord.ext import commands
from bmi_calc import calculate_bmi 
import datetime
import asyncio 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents, help_command=None)

def get_conversion_rate(from_currency, to_currency):
    api_key = "cc235b366f7a312cc5099fca"
    url = f"https://v6.exchangerate-api.com/v6/cc235b366f7a312cc5099fca/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    print(data)
    
    if 'conversion_rates' in data:
        rates = data['conversion_rates']
        if to_currency in rates:
            return rates[to_currency]
        else:
            print(f"Rate for {to_currency} was not found")

    else:
        print("Key 'conversion_rates' not found in response.")
        return None


@bot.event
async def on_ready():
    print(f"Yoo, I'm {bot.user.name}, and I'm ready!")

@bot.command(name='admatai')
async def timer(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("מה השנת שחרור?")
    year_msg = await bot.wait_for(f'message', check=check, timeout=60)
    year = int(year_msg.content)

    await ctx.send("מה החודש שחרור?")
    month_msg = await bot.wait_for(f'message', check=check, timeout=60)
    month = int(month_msg.content)

    await ctx.send("מה היום שחרור?")
    day_msg = await bot.wait_for(f'message', check=check, timeout=60)
    day = int(day_msg.content)

    target_date = datetime.datetime(year, month, day)
    now = datetime.datetime.now()

    if target_date <= now:
        await ctx.send("שלא תדע עוד צה״ל!")
        return

    # while True:
    now = datetime.datetime.now()
    remaining_time = target_date - now
    days = remaining_time.days
    
    if days >= 1100:
        await ctx.send (f"""{days} ימים לשחרור.
        חתמת, סתמת. """)
        return
        
    elif 1099 >= days >= 730:
        await ctx.send (f"""{days} ימים לשחרור.
        לך תעשה כביסה למדים שלך
        יש לך ריח של בקוםם""")
        return

    elif 729 >= days >= 365:
        await ctx.send (f"""{days} ימים לשחרור.
        צעיר מושתן אתה.
        לך תעשה כלים.""")
        return

    elif 364 >= days >= 100:
        await ctx.send (f"""{days} ימים לשחרור.
        יום יבוא אחי. אל תדאג""")
        return        

    elif 99 >= days >= 31:
        await ctx.send (f"""{days} ימים לשחרור.
        עד מתי?? פחות ממאה יום!""")
        return                

    elif 30 >= days >= 7:
        await ctx.send (f"""{days} ימים לשחרור.
        כמה עוד?? פחות מחודש!!""")
        return        

    elif 6 >= days >= 2:
        await ctx.send (f"""{days} ימים לשחרור.
        מריח כבר את הסוף?
        קוראים לזה אזרחות. קונספט מגניב.""")
        return        

    elif 2 >= days >= 0:
        await ctx.send (f"""{days} ימים לשחרור.
        שנהייה לחמאס ולא ולצה״ל! 
        :D""")
        return        


        # await ctx.send(f"""עד מתי {target_date.date()}?!
        # {days}  ימים 
        # כי לחופש יש תאריך 🥲 """)
        # break


        # if remaining_time.total_seconds() <= 0:
        #     await ctx.send("Time's up!")
        #     break

        # await asyncio.sleep(60)  # Update every 60 seconds
        
@bot.command()
async def help(ctx):
    help_message = """Welcome to Ad Matai. 
    Avalible Commands:
    ?calc - the best calc on the market (calc is short for calculator chat).
    ?bmi - see how fat you are.
    ?admatai 'year' 'month' 'day' - shows how long you have to suffer.
    ?convert [amount] [From currency] [To currency]
    ?help - shows this message."""
    await ctx.send(help_message)

@bot.command()
async def bmi(ctx):
    while True:
        await ctx.send("Please enter ur kilos u fattie: ")

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        try:
            weight_msg = await bot.wait_for('message', check=check, timeout=60.0)
            weight = float(weight_msg.content)
        except Exception as e:
            await ctx.send("Invalid input or timed out. Please try again.")
            return

        # Ask the user for their height
        await ctx.send("Please enter your height in meters:")

        try:
            height_msg = await bot.wait_for('message', check=check, timeout=60.0)
            height = float(height_msg.content)
        except Exception as e:
            await ctx.send("Invalid input or timed out. Please try again.")
            return


        # Calculate BMI
        bmi = weight / (height ** 2)
        if bmi <= 18.5:
            category = "underweight"
        elif 18.6 <= bmi <= 24.9:
            category = "normal"
        elif 25 <= bmi <= 29.9:
            category = "overweight"
        elif bmi >= 30:
            category = "obease"
        else:
            category = "wtf"

        await ctx.send(f"hey {ctx.author.mention}, your BMI is {bmi:.2f}. which is {category}")

        await ctx.send(f"would you like to calculate again? (yes/no)")

        newbmi = await bot.wait_for('message', check=check, timeout=60)
        newbmi_msg = str(newbmi.content)
        
        if newbmi_msg == 'yes':
            await ctx.send("Calculating again.")
        else:
            await ctx.send("Aight. Goodbye")
            break

            

    # await ctx.send(f"Your BMI is {bmi:.2f}")

@bot.command()
async def calc(ctx):
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        if y == 0:
            return "Error: Division by zero!"
        else:
            return x / y
            
    await ctx.send("enter your first number: ")

    while True:
        try:
            number1_msg = await bot.wait_for('message', check=check, timeout=60.0)
            num1 = float(number1_msg.content)
            if num1.is_integer():
                num1 = int(num1)
                break
            else:
                num1 = float(num1)
                break
        except ValueError:
                await ctx.send("Please enter only numbers.")
        except Exception as d:
            await ctx.send("Timed out.")
            return
    
    
    while True:
        await ctx.send(f"Your current number is {num1}. Whats the second number?")

        while True:
            try:
                number2_msg = await bot.wait_for('message', check=check, timeout=60.0)
                num2 = float(number2_msg.content)
                if num2.is_integer():
                    num2 = int(num2)
                    break
                else:
                    num2 = float(num2)
                    break
            except ValueError:
                    await ctx.send("Please enter only numbers.")
            except Exception as d:
                await ctx.send("Timed out.")
                return
        
        await ctx.send(f"So your second number is {num2}. what action do you want?: (subtract/add/multiply/divide)")

        while True:
            action_msg = await bot.wait_for('message', check=check, timeout=60.0)
            action = str(action_msg.content)

            if action.isalpha():
                break
            else:
                await ctx.send("Please enter only add/subtract/multiply/divide.")
        
        if action == 'add':
            result = add(num1, num2)
        if action == 'subtract':
            result = subtract(num1, num2)
        if action == 'multiply':
            result = multiply(num1, num2)
        if action == 'divide':
            result = divide(num1, num2)
            
            
        await ctx.send(f"{num1} {action} {num2} = {result}")
        await ctx.send("Do you want to perform another calculation? (yes/no)")
        try:
            continue_msg = await bot.wait_for('message', check=check, timeout=60)
            if continue_msg.content.lower() == 'yes':
                num1 = result
            else:
                break
        except Exception as d:
            await ctx.send("Timed out.")
            break
    

    await ctx.send("Calculation ended.")

@bot.command()
async def convert(ctx, amount: float, from_currency: str, to_currency: str):
    try:
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()

        rate = get_conversion_rate(from_currency, to_currency)
        if rate:
            converted_amount = amount * rate
            await ctx.send(f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
        else:
            await ctx.send("Invalid Currency Code.")

    except (IndexError, ValueError):
        await ctx.send('Usage: ?convert <amount> <from_currency> <to_currency>')








    




    
    
    





# @bot.command()
# async def bmi(ctx, weight: float, height: float):
#     result = calculate_bmi(weight, height)
#     await ctx.send(f"Hey {ctx.author.mention}, {result}")

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


