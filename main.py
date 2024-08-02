from discord.ext import commands
import discord
import requests

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    
    print(f'We have logged in as {client.user}')
    print("------------------------------")

@client.command()
async def hello(ctx):
    await ctx.send("Hello!, I am Kimochu.bot. I'm more like Chat GPT but you can say I am the downgrade of gpt 3.5 turbo. I am still under development")

@client.command()
async def goodbye(ctx):
    await ctx.send('Goodbye!, hope you have a good rest of the day')

@client.command()
async def time(ctx):
    await ctx.send('The time is 2:00pm')

@client.event
async def on_member_join(member):
    channel = client.get_channel('USER_ID')
    await channel.send("Welcome")

@client.event
async def on_member_remove(member):
     channel = client.get_channel('USER_ID')
     await channel.send("Goodbye")



client.run('TOKEN_KEY')




















# import discord
# from discord.ext import commands

# client = commands.Bot(command_prefix = '!')

# @client.event
# async def on_ready():
#     print("The bot is now ready for use!")
#     print("------------------------------")

# @client.command()
# async def hello(ctx):
#     await ctx.send("Hello, I am KImochu.bot")


# client.run('MTI2ODUwMjU4NjQ5MTY3MDU2MQ.GFyD5b.xUYXHXazxh1jInAhRXMuV94jY84JmVUbtU9hu4')
