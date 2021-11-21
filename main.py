#910330805660811315 client id
#OTEwMzMwODA1NjYwODExMzE1.YZRRoQ.MfpZSIiLYFwqQBiZSfiSyjcPVrw  token
#permision 8

import discord

from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL

from discord.ext import commands
from datetime import datetime, timedelta

#client = discord.Client()

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix = '!', help_command= None)

#wrapper/decorator
@bot.event
async def on_ready():    #async การทำงานที่ไม่พร้อมกัน ทำงานโดยไม่ต้องรอ
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, * ,par ): #ctx=contect, par is รับtext, * รับประโยค
    await ctx.channel.send("I'm here {0}".format(par))

@bot.command()
async def Bro(ctx):
    await ctx.channel.send("I'm here")

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="Lufy bot help", description="All avaliable bot commands", color=0xff0000)
    emBed.add_field(name= "help", value = "Get help commands", inline=False)
    emBed.add_field(name= "test", value = "Respond message that you've send", inline=False)
    emBed.add_field(name= "Bro", value = "Send I'm here message to user", inline=False)
    emBed.set_thumbnail(url='https://f.ptcdn.info/814/039/000/o1zg661fdlB22bw5b5a-o.jpg')
    emBed.set_footer(text="Good luck Bro!", icon_url='https://www.freepik.com/free-icon/python_15116801.htm#page=1&query=python&position=5&from_view=search')
    await ctx.channel.send(embed = emBed)


@bot.event
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == 'Say hi':   #ออนเมสเสจเจอแล้วตรง ให้ส่งข้อความกลับ
        await message.channel.send('Hello')    # .channel.send ส่งห้องไหนห้องนั้น
        #await ใช้ได้กับบางฟังก์ชั่นเท่านั้น ต้องรอทำawaitเสร็จก่อน
    elif message.content == 'Hello Bro':
        await message.channel.send(str(message.author.name) + ' Hello')
    elif message.content == 'นายชื่ออะไรอะ' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds = 10)
        await message.channel.send('เราชื่อ ' + str(bot.user.name))
        #logging
        print('{0} เรียกใช้ นายชื่ออะไร เวลา {1} จะใช้ได้อีกทีตอน {2}' .format(message.author.name, datetime.now(), message_lastseen))

    elif message.content == 'เราชื่ออะไร' and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds = 10)
        await message.channel.send('นายก็ชื่อ ' + str(message.author.name) + 'ไง')
        print('{0} เรียกใช้ เราชื่ออะไร เวลา {1} จะใช้ได้อีกทีตอน {2}' .format(message.author.name, datetime.now(), message2_lastseen))
    elif message.content == '!logout':
        await message.channel.send('Good bye...')
        await bot.logout()
    await bot.process_commands(message)

@bot.command()
async def play(ctx, url):
    channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    if voice_client == None:
        ctx.channel.send('Joined')
        await channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)

    YDL_OPTIONS = {'format' : 'bestaudio', 'noplaylist' : 'True'}
    FFMPEG_OPTIONS = {'before_options' : '-reconnect_streamed 1 -reconnect_delay_max_5', 'options' : '-vn'}

    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        #voice = get(self.bot.voice_clients, guild=ctx.guild)
        voice_client.play(discord.FFmpegPCMAudio(URL))
        voice_client.is_playing()
    else:
        await ctx.channel.send("Already playing song")

@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    

    

bot.run('OTEwMzMwODA1NjYwODExMzE1.YZRRoQ.MfpZSIiLYFwqQBiZSfiSyjcPVrw')