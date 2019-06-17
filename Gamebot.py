import discord
import asyncio

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
        embed.add_field(name='`나머지는', value='시험끝나고 내일 한다.', inline=False)

app.run(token)
