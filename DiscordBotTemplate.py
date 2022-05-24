import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import time
import asyncio

total_timers = 0
total_flashcards = 0
total_tasks = 0
timers = 0
pomodorotimer = 45
breaktimer = 15
stuffToDo = []
timesToDoIt = []
CR = []
AN = []

my_secret = os.environ['my_secret']
bot = commands.Bot(command_prefix='.')

load_dotenv()


@bot.command()
##input
async def Help(ctx):
    ##reply output
    await ctx.reply('.pomodoro_timer, .toDo, .flashCards, .achievements')



@bot.command()
async def achievements(ctx):
  global total_timers
  global total_flashcards
  global total_tasks
  global timers
  while True:
    await ctx.send(f"Do you want to see your achievements (Y/N)? ")
  
    def check(msg):
        return msg.author == ctx.author and msg.channel == ctx.channel

    msg = await bot.wait_for("message", check=check)
    userinput1 = msg.content.upper()

    
    if (userinput1 == "Y"):
      await ctx.send("\nYou studied for "+str(total_timers*45) + " minutes")
      await ctx.send("You made "+str(total_flashcards) + " flashcards")
      await ctx.send("You finished  "+str(total_tasks) + " tasks")
      return;
    elif (userinput1 == "N"):
      return;
    else:
      await ctx.send("\n Please type Y or N.")
