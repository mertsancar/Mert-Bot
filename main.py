import discord
import random
from keep_alive import keep_alive
import data_processing


meals = (data_processing.meals)
filmdizi =(data_processing.filmdizi)

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content == '-mertbot help':
        temp = ['-mertbot naber','-mertbot wiki','-mertbot film','-mertbot dizi','-mertbot neyesek','-mertbot teşekkürler']

        for item in temp:
          await message.channel.send(item)
    
    if message.content == '-mertbot':
        await message.channel.send('Merhaba ben MertBot!')


    if message.content == '-mertbot naber':
        naber_cevap = ["iyim sen?","şüpeeeeer sen?","takılıyoz işte sen? "]
        await message.channel.send(naber_cevap[random.randint(0,2)])


    if message.content.startswith('-mertbot wiki'):
        msg = message.content.split("-mertbot wiki ")
        await message.channel.send("https://tr.wikipedia.org/wiki/{0}".format(msg[1]))


    if message.content.startswith('-mertbot film'):
        temp = []
        
        for film in filmdizi:
          if film[1] == "Film":
            temp.append(film)

        _film = temp[random.randint(0,len(temp)-1)]

        await message.channel.send(_film[0])
        await message.channel.send(_film[2])

    if message.content.startswith('-mertbot dizi'):
        temp = []

        for dizi in filmdizi:
          if dizi[1] == "Dizi":
            temp.append(dizi)

        _dizi = temp[random.randint(0,len(temp)-1)]

        await message.channel.send(_dizi[0])
        await message.channel.send(_dizi[2])
   

    if message.content.startswith('-mertbot neyesek'):
        param = message.content.split("-mertbot neyesek ")
        param = param[1].split(" ")

        temp = []
        for meal in meals:
             
          if meal[1] == int(param[0]) and meal[2] == int(param[1]):
            temp.append(meal[0])

 
        await message.channel.send(temp[random.randint(0,len(temp))])    


    if message.content == '-mertbot teşekkürler':
        thanks_cevap = ["Ne demek her zaman :)","Yine bekleriz","Ricaaaaa"]
        await message.channel.send(thanks_cevap[random.randint(0,len(thanks_cevap)-1)])
        

        


keep_alive()        
client.run("ODI1OTc4MzY2NzQ5NTczMTcw.YGFyTA.zuaC_4SB2MGgvL8sc1N58SXLI2o")


      
