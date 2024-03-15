import discord, asyncio
import requests
import os
from io import BytesIO
from discord.ext import commands
from PIL import Image, ImageSequence
import pocket

TOKEN = pocket.TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.messages = True

bot = commands.Bot(command_prefix='`', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    # 메시지가 이미지를 포함하고, 그 메시지가 원하는 채널에서 온 경우
    if message.attachments :
        for attachment in message.attachments:
            # 파일 이름에서 확장자를 추출
            # print(attachment.filename)
            filename, file_extension = attachment.filename.split('.')
            file_url = attachment.url

            # 각 첨부 파일의 MIME 타입을 확인하여 이미지인지 판단
            if file_extension == 'webp' :
                # 여기에서 이미지에 대한 원하는 동작을 수행
                responese = requests.get(file_url)
                img = Image.open(BytesIO(responese.content))
                index = 0

                # 움짤 여부 확인
                for frame in ImageSequence.Iterator(img) :
                    index += 1
                    if index == 2 :
                        break
                if index > 1 :
                    # gif 이미지
                    img.info.pop('background', None)
                    img.save(f'./image/{filename}.gif', 'gif', save_all=True)
                    filepath = f'./image/{filename}.gif'
                    img.close()

                    # 이미지 전송
                    try :
                        await message.reply(file=discord.File(filepath))
                        os.remove(filepath)
                    except :
                        await message.reply(f'이미지 용량이 너무 커 변환에 실패했습니다!')
                        os.remove(filepath)

    # 커맨드 활성화
    await bot.process_commands(message)

@bot.command(name='영역전개')
async def ryoiki(ctx) :
    imgpath = './image/sukuna/sukuna.png'
    img_file = discord.File(imgpath, filename="sukuna.png")
    
    embed = discord.Embed(title="료멘스쿠나", description="", color=0x8B0000)
    embed.set_thumbnail(url="attachment://sukuna.png")
    embed.add_field(value="좋은 기회니까 친히 가르쳐주지.", name="", inline=False)
    embed.add_field(value="진짜 주술이라는 것을 말이야.", name="", inline=False)
    embed.add_field(value="", name="", inline=False)
    embed.add_field(value="", name="영역 전개ーー", inline=False)

    gifpath = './image/sukuna/sukuna.gif'
    gif_file = discord.File(gifpath, filename="sukuna.gif")
    embed2 = discord.Embed(title="료멘스쿠나", description="", color=0x8B0000)
    embed2.add_field(value="", name="복마어주자 【伏魔御廚子】", inline=False)
    embed2.set_image(url="attachment://sukuna.gif")

    await ctx.send(embed=embed, file=img_file)
    await ctx.send(embed=embed2, file=gif_file)

@bot.command(name='만해')
async def itkaku(ctx) :
    img1_filepath = './image/itkaku/itkaku.png'
    img2_filepath = './image/itkaku/itkaku_bankai.jpg'

    img1_file = discord.File(img1_filepath, filename="itkaku_normal.png")
    img2_file = discord.File(img2_filepath, filename="itkaku_bankai.jpg")

    embed_1 = discord.Embed(title="마다라메 잇카쿠", description="", color=0x00BFFF)
    embed_1.set_thumbnail(url="attachment://itkaku_normal.png")
    embed_1.add_field(value="아- 아-", name="", inline=False)
    embed_1.add_field(value="이런 데서 쓰고 싶진 않았는데!", name="", inline=False)
    embed_1.add_field(value="똑똑히 봐둬라.", name="", inline=False)
    embed_1.add_field(value="그리고 아무한테도 말하지 마라!", name="", inline=False)
    
    embed_2 = discord.Embed(title="마다라메 잇카쿠", description="", color=0x00BFFF)
    embed_2.set_image(url="attachment://itkaku_bankai.jpg")
    embed_2.add_field(name="만해!! [卍解]", value="", inline=False)

    await ctx.send(embed=embed_1, file=img1_file)
    await ctx.send(embed=embed_2, file=img2_file)
    #await ctx.send(file=discord.File(filepath))

@bot.command(name='배드애플')
async def badapple(ctx) :
    badapple_video = open('./text/badapple_edit.txt', 'r')
    badapple_text = badapple_video.read()
    badapple_scenes = badapple_text.split("SPLIT")

    msg = await ctx.send(badapple_scenes[0])
    for badapple_scene in badapple_scenes :
        await asyncio.sleep(0.1)
        await msg.delete()
        msg = await ctx.send(badapple_scene)



bot.run(TOKEN)