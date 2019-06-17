import discord
import asyncio
import random
import openpyxl
from discord import Member
import youtube_dl
import bs4
import os
import sys
import json
from selenium import webdriver
import random

app = discord.Client()

token = "NTkwMTc2MjYyMDc3ODA4NjU5.XQebJg.IgIw0Dr0Fj4pOoQnQO2eG96avG4"

@app.event
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("=========")
    await app.change_presence(game=discord.Game(name="`마재", type=2))

@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "`마재":
        await app.send_message(message.channel, "내가 가장 좋아하는 스트리머!!")
    if message.content == "`명령어":
        embed = discord.Embed(title="명령어 목록", description="명령어 목록입니닷!", colour = discord.Colour.blue())
    
        #embed.set_footer(text = "추가명령어는 토끼린에게 문의바람")
        embed.add_field(name='`마재', value='평소의 겜맨입니다.', inline=False)
        embed.add_field(name='`고양이', value='고양이 사진이 나옵니다..', inline=False)
        embed.add_field(name='`강아지', value='강아지 사진이 나옵니다.', inline=False)
        embed.add_field(name='`네코', value='2D 고양이 이미지가 나옵니다', inline=False)
        embed.add_field(name='`나머지는', value='시험끝나고 내일 한다.', inline=False)

    if message.content.startswith('^고양이'):
        embed = discord.Embed(
            title='고양이는',
            description='멍멍',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await app.send_message(message.channel, embed=embed)

    if message.content.startswith('^강아지'):
        embed = discord.Embed(
            title='강아지는',
            description='야옹야옹',
            colour=discord.Colour.green()
        )

        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum = random.randrange(1, 30977)
        urlF = urlBase+str(randomNum)
        embed.set_image(url = urlF)
        await app.send_message(message.channel, embed=embed)
        
        if message.content.startswith('^네코'):
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed2 = discord.Embed(
            colour=discord.Colour.green()
        )
        embed3 = discord.Embed(
            colour=discord.Colour.green()
        )
        randomnumber = random.randrange(100, 407)
        randomgiho = random.randrange(1,3)
        print('?번째사진 : '+str(randomnumber))
        print('기호 : '+str(randomgiho))
        strandomnumber = str(randomnumber)
        file1 = '.png'
        file2 = '.jpg'
        file3 = '.jpeg'
        giho = '_'
        if randomgiho==1:
            urlbase1 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file1
            urlbase2 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file2
            urlbase3 = "https://cdn.nekos.life/neko/neko" + strandomnumber + file3
            embed.set_image(url=urlbase1)
            embed2.set_image(url=urlbase2)
            embed3.set_image(url=urlbase3)
            await app.send_message(message.channel, embed=embed)
            await app.send_message(message.channel, embed=embed2)
            await app.send_message(message.channel, embed=embed3)
        else:
            urlbase_1 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file1
            urlbase_2 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file2
            urlbase_3 = "https://cdn.nekos.life/neko/neko" + giho + strandomnumber + file3
            embed.set_image(url=urlbase_1)
            embed2.set_image(url=urlbase_2)
            embed3.set_image(url=urlbase_3)
            await app.send_message(message.channel, embed=embed)
            await app.send_message(message.channel, embed=embed2)
            await app.send_message(message.channel, embed=embed3)

app.run(token)
