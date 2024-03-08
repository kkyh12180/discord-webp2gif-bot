import discord
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

bot = commands.Bot(command_prefix='$', intents=intents)

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
                        await message.channel.send(f'이미지 용량이 너무 커 변환에 실패했습니다!')

                '''
                else :
                    # png 이미지
                    img.save(f'./image/{filename}.png', 'png')
                    filepath = f'./image/{filename}.png'
                    img.close()

                    # 이미지 전송
                    try :
                        await message.reply(file=discord.File(filepath))
                        os.remove(filepath)
                    except :
                        await message.channel.send(f'이미지 용량이 너무 커 변환에 실패했습니다!')
                '''

bot.run(TOKEN)