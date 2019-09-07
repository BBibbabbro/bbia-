#-*- coding:utf-8 -*- 
import asyncio
import discord
import datetime
import random
from urllib.request import urlopen, Request
import urllib
import urllib.request
from discord import Member
from discord.ext import commands
import os
import sys
import json
import time
import html.parser
import html
import bs4
import urllib
import urllib.request
import pip._internal.locations
import learn

client = discord.Client() 

# 토큰입력
token = "NjE4MTUwMjcwNTgwNDI0Nzkz.XW1fkQ.K5hMGirBAsZEHFHAqEw-wAl1sM8"

# 봇이 켜졌을때
@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("=도움말")
    await client.change_presence(status=discord.Status.idle, activity=game)

# 봇이 새로운 메시지를 수신했을때

@client.event
async def on_message(message):
    if message.content.startswith("=도움말"):
        embed = discord.Embed(title="=j│현재 채널에 봇을 추가 시킵니다.", description="=p│노래이름 = 해당 노래를 재생 합니다.", color=0x00ff00)
        embed.set_footer(text = "!j = 현제 채널에 봇을 추가 시킵니다!")
        embed.set_footer(text = "!p 노래이름│해당 노래를 재생 합니다!")
        embed.set_footer(text = "!skip│해당 노래를 스킵 힙니다!")
        embed.set_footer(text = "=s│현재 노래를 스킵 합니다.")
        #embed.add_field(name="이름", value=message.author.name, inline=True)
        #embed.add_field(name="닉네임", value=message.author.display_name, inline=True)
        #embed.add_field(name="고유번호", value=message.author.id, inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("=도움말"):
        embed = discord.Embed(title="=영화순위│Top20 영화순위를 알려줍니다", description="=주사위│1 부터 6 까지 수중 하나를 뽑습니다.", color=0x00ff00)
        embed.set_footer(text = "!j = 현제 채널에 봇을 추가 시킵니다!")
        embed.set_footer(text = "!p 노래이름│해당 노래를 재생 합니다!")
        embed.set_footer(text = "!skip│해당 노래를 스킵 힙니다!")
        embed.set_footer(text = "=정보│내 정보를 알아봅니다.")
        #embed.add_field(name="이름", value=message.author.name, inline=True)
        #embed.add_field(name="닉네임", value=message.author.display_name, inline=True)
        #embed.add_field(name="고유번호", value=message.author.id, inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("=정보"):
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(color=0x00ff00)
        embed.add_field(name="닉네임", value=message.author.name, inline=True)
        embed.add_field(name="서버 닉네임", value=message.author.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일")
        embed.add_field(name="고유번호", value=message.author.id)
        await message.channel.send(embed=embed)

    if message.content.startswith('=이모티콘'):

        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "] # 이모티콘 배열입니다.

        randomNum = random.randrange(0, len(emoji)) # 0 ~ 이모티콘 배열 크기 중 랜덤숫자를 지정합니다.
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])
        embed = discord.Embed(color=0x00ff00)
        await message.channel.send(embed=discord.Embed(description=emoji[randomNum])) # 랜덤 이모티콘을 메시지로 출력합니다
    
    #if message.content.startswith('=도움말'):
        #msg = ' ```노래 봇 기능 이외에도``` '.format(message)
        #await message.channel.send(msg)

    #if message.content.startswith('=도움말'):
        #msg = ' ```=정보 / =영화순위 / =복권 / =주사위 / =이모티콘``` '.format(message)
        #await message.channel.send(msg)

    #if message.content.startswith('=도움말'):
        #msg = ' ```같은 명령어가 있습니다.``` '.format(message)
        #await message.channel.send(msg)

    if message.content.startswith('아야야!'):
        embed = discord.Embed(title="아야야!", description="", color=0xF4FA58)
        await message.channel.send(embed=embed)

    if message.content.startswith('넌 누'):
        embed = discord.Embed(title="난 존나 쓸대없이 만들어진 아야야 봇 이야!", description="", color=0xF4FA58)
        await message.channel.send(embed=embed)

    if message.content.startswith('애기 안녕'):
        embed = discord.Embed(title="안농~", description="", color=0xFF00DD)
        await message.channel.send(embed=embed)

    if message.content.startswith("=복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="1회차 복권",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(embed=embed)

    if message.content.startswith('=주사위'):

        randomNum = random.randrange(1, 7) # 1~6까지 랜덤수
        print(randomNum)
        if randomNum == 1:
            await message.channel.send(embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await message.channel.send(embed=discord.Embed(description=':game_die: ' + ':six: '))

    if message.content.startswith("!일기예보"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'일기예보')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태



        await message.channel.send(embed=embed)

    if message.content.startswith('=영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
        i1 = 0 # 랭킹 string값
        embed = discord.Embed(
            title = "영화순위",
            description = "Top 20 위 영화 순위 입니다.",
            colour= discord.Color.purple()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1+1
            stri1 = str(i1) # i1은 영화랭킹을 나타내는데 사용됩니다
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
            print()
            embed.add_field(name='-Top '+stri1+' 위', value='\n영화제목 : '+moviechartLi1MovieName+'\n평점 : '+moviechartLi1Ratting+'점'+'\n개봉날짜 : '+moviechartLi1openDay+'\n예매율,랭킹변동 : '+moviechartLi1Yerating, inline=False) # 영화랭킹


        await message.channel.send(embed=embed)

    if message.content.startswith("=명령어"):
        channel = message.channel
        embed = discord.Embed(
            title = '명령어들이다 크크크큭',
            description = '각각의 명령어들 이다 잘 봐둬라 큭...',
            colour = discord.Colour.blue()
        )

        #embed.set_footer(text = '끗')
        dtime = datetime.datetime.now()
        #print(dtime[0:4]) # 년도
        #print(dtime[5:7]) #월
        #print(dtime[8:11])#일
        #print(dtime[11:13])#시
        #print(dtime[14:16])#분
        #print(dtime[17:19])#초
        embed.set_footer(text=str(dtime.year)+"년 "+str(dtime.month)+"월 "+str(dtime.day)+"일 "+str(dtime.hour)+"시 "+str(dtime.minute)+"분 "+str(dtime.second)+"초")
        #embed.set_footer(text=dtime[0:4]+"년 "+dtime[5:7]+"월 "+dtime[8:11]+"일 "+dtime[11:13]+"시 "+dtime[14:16]+"분 "+dtime[17:19]+"초")
        embed.add_field(name= '!안녕', value = '인사하고싶을때 ㄱㄱ',inline = False)
        embed.add_field(name='!오늘배그', value='오늘 배그각 알려줌', inline=False)
        embed.add_field(name='!홋치', value='!홋치 단어1 단어2 형식으로 적으면 학습함', inline=False)
        embed.add_field(name='!말해', value='!말해 단어1 형식으로 적으면 학습한내용 말함', inline=False)
        embed.add_field(name='!기억초기화', value='학습한 데이터 초기화함', inline=False)
        embed.add_field(name='!데이터목록', value='학습한 데이터목록 알려줌', inline=False)
        embed.add_field(name='!모두모여', value='모두를 언급함', inline=False)
        embed.add_field(name='!들어와', value='봇이 음성채널에 들어옴', inline=False)
        embed.add_field(name='!나가', value='봇이 음성채널에 나감', inline=False)
        embed.add_field(name='!재생', value='!재생 유튜브링크 형식으로 적으면 유튜브 틀어줌', inline=False)
        embed.add_field(name='!일시정지', value='재생중인 유튜브 일시정지함', inline=False)
        embed.add_field(name='!다시재생', value='정지중인 유튜브 다시 재생함', inline=False)
        embed.add_field(name='!멈춰', value='재생,정지중인 유튜브 없어짐(영상목록 초기화)', inline=False)
        embed.add_field(name='!날씨', value='!날씨 원하는지역 을 입력하면 그 지역의 날씨정보를 제공합니다.', inline=False)
        embed.add_field(name='!롤', value='!롤 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그솔로', value='!배그솔로 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그듀오', value='!배그듀오 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!배그스쿼드', value='!배그스쿼드 닉네임 형식으로 적으면 그 닉네임에대한 정보를 알려줍니다..', inline=False)
        embed.add_field(name='!고양이', value='!고양이 라고 적으면 고양이 사진이 나옵니다..', inline=False)
        embed.add_field(name='!강아지', value='!강아지 라고 적으면 강아지 사진이 나옵니다.', inline=False)
        embed.add_field(name='!네코', value='!네코 라고 적으면 2D 고양이 이미지가 나옵니다', inline=False)
        embed.add_field(name='!실시간검색어, !실검', value='!실시간검색어, !실검 이라고 적으면 네이버의 실시간 검색어 순위가 나타납니다.', inline=False)
        embed.add_field(name='!번역 번역할문자', value='!번역 번역할문자 이라고 적으면 번역할 문자를 번역한 링크가 나타납니다. ("띄어쓰기를 하시면 안됩니다. _,-등으로 구분해주세요.")', inline=False)
        embed.add_field(name='!영화순위', value='영화를 1~20순위로 나눈 영화순위 정보를 제공합니다.', inline=False)
        embed.add_field(name='!급식', value='군포e비즈니스 고등학교의 급식정보를 제공합니다.', inline=False)
        embed.add_field(name='!복권', value='랜덤으로 선정한 복권번호를 메시지로 보내줍니다.', inline=False)
        embed.add_field(name='!검색', value='!검색 검색할키워드 형식으로 입력하시면 유튜브 검색결과를 메시지로 보내줍니다.', inline=False)





#@client.event
#async def on_message(message):
#    if message.content.startswith("!dddd"):
 #       embed = discord.Embed(title="내 정보", description="내 정보를 표시 합니다.", color=0x00ff00)
  #      embed.set_footer(text = "!j = 현제 채널에 봇을 추가 시킵니다!")
   #     embed.set_footer(text = "!play 노래이름│해당 노래를 재생 합니다!")
    #    embed.set_footer(text = "!skip│해당 노래를 스킵 힙니다!")
     #   embed.set_footer(text = "")
      #  embed.add_field(name="이름", value=message.author.name, inline=True)
       # embed.add_field(name="닉네임", value=message.author.display_name, inline=True)
        #embed.add_field(name="고유번호", value=message.author.id, inline=True)
        #await message.channel.send(embed=embed)


@client.event
async def on_reaction_add(reaction, user):
    if str(reaction.emoji) == "👊":
        await reaction.message.channel.send(user.name + " 님이 죽빵을 때리셨습니다, 아야.")
    if str(reaction.emoji) == "🤛":
        await reaction.message.channel.send(user.name + " 님이 왼쪽으로 한대 때리셨습니다, 아야.")
    if str(reaction.emoji) == "🤜":
        await reaction.message.channel.send(user.name + " 님이 오른쪽 으로 한대 때리셨습니다, 아야.")




    

client.run(token)