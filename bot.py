import discord
import json
import random
from Yandex import Translate

translate = Translate(api_key='translate_api_key')

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))



    async def on_message(self, message):
        global numberoft
        if str(message.channel.id) == '613134424757895187':
            if message.author != client.user:
                if message.content.startswith('<<iterations'):
                    strsplit = message.content.split()
                    numberoft = int(strsplit[1])
                    await message.channel.send('Number of iterations set to ' + strsplit[1])
                    return;
                translatedText = message.content
                for i in range(numberoft):
                    l1 = random.randint(1, 93)
                    with open('languaged.json') as lang_strings:
                        data = json.load(lang_strings)
                        languagesd = data[str(l1)]
                    translatedText = translate.translate(translatedText, languagesd)
                    print(translatedText)

                translatedText2 = translate.translate(translatedText, 'en')
                await message.channel.send(translatedText2)

client = MyClient()
client.run('Discord_bot_token')
