import discord
import os 
os.chdir("C:/Users/cynth/Downloads/")
import asyncio
from honkaistarrail import starrail

intents = discord.Intents.all()
client = discord.Client(intents=intents) 

#set bot status and intialize  
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('!d help'))
    print('We have logged in as {0.user}'.format(client))

#hsr warp history
async def get_warp_history():
    link = ""
    async with starrail.Jump(link = link,banner = 1,lang = "en") as hist:
        async for key in hist.get_history():
            for info in key:
                print(f'[{info.type}] Name: {info.name} ({info.rank}*) - {info.time.strftime("%d.%m.%Y %H:%M:%S")}')


@client.event
async def on_message(message):
    print("message-->", message)
    if message.author == client.user:
        return
    if message.content.startswith('!d update'):
        directions = discord.Embed(title="Update player wish history", description="Import your wish history and paste your warp URL into this DM. Instructions can be found at https://starrailstation.com/en/warp#import", 
                                   color=0x00ff00)
        await message.author.send(embed=directions)
        if message.content.startswith('https://api-os-takumi.mihoyo.com/common/gacha_record/api/getGachaLog?'):
            await.message.author.send('Warp history has been updated.')
#channel command responses 
    if message.content.startswith('!d help'):
        command_list = discord.Embed(title="Help", description="List of commands", color=0x00ff00)
        command_list.add_field(name="!d update", value="Update your warp history", inline=False)
        command_list.add_field(name="!character [character name]", value="Build for [character name]; infographics made by MELLOONA on HoyoLab. Use '!character trailblazer [element] for trailblazer", inline=False)
        command_list.add_field(name="!warp", value="Gives summary of warp history, including pity count", inline=False)
        command_list.add_field(name='!pity', value='Returns number of warps needed to guarantee the featured 5*', inline=False)
        await message.channel.send(embed=command_list)
    #character builds 
    elif message.content.startswith('!character dan heng'):
        await message.channel.send(file=discord.File('dan heng info.webp'))
    elif message.content.startswith('!character march 7th'):
        await message.channel.send(file=discord.File('march 7th info.webp'))
    elif message.content.startswith('!character natasha'):
        await message.channel.send(file=discord.File('natasha info.webp'))
    elif message.content.startswith('!character dan heng'):
        await message.channel.send(file=discord.File('dan heng info.webp'))
    elif message.content.startswith('!character trailblazer physical'):
        await message.channel.send(file=discord.File('tb phys info.webp'))
    #warp tracking
    if message.content.startswith(

