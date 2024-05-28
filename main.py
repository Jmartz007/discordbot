from dotenv import load_dotenv
import discord


import os

load_dotenv()

token = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)



@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online")

@bot.event
async def on_message(message: discord.Message):
    print(message.author)
    print(message.author.id)
    print(message.content)
    # print(type(message.mentions))
    # print(type(message.mentions[0]))
    print(message.mentions)

    if message.author.id == 1210072404861263912:
        print("bot sent message")
        pass
    elif "member biff" in  message.content:
        # await message.channel.send("")
        await message.reply("nope")

    elif "mike" in message.content:
        await message.reply("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3duODl1ajRxcWUwbWh1cm1rN240cjV0OGw2dGQ1MGdvbXdtbG1sYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orieX60fpk4DuYPkY/giphy.gif")
    
    elif message.mentions:
        for mention in message.mentions:
            if  "justbringit995" in  mention.name:
                await message.reply("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3duODl1ajRxcWUwbWh1cm1rN240cjV0OGw2dGQ1MGdvbXdtbG1sYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3orieX60fpk4DuYPkY/giphy.gif")
                print("----------")




@bot.slash_command(name="hello", description="Say hello to the bot")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExa2xicWpqY2N0dWozeXVuYXdyNnhsdDU4eG5oY3d6OHZuMHhtMGp3cSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Nx0rz3jtxtEre/giphy.gif")

bot.run(token)