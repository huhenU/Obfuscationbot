import discord
import json
import random
from googletrans import Translator

translator = Translator()

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))



    async def on_message(self, message):
        global numberoft
        if str(message.channel.id) == 'channel_id':
            if message.author != client.user:
                if message.content.startswith('<<iterations'):
                    strsplit = message.content.split()
                    numberoft = int(strsplit[1])
                    await message.channel.send('Number of iterations set to ' + strsplit[1])
                    return;
                originalText = message.content
                for i in range(numberoft):
                    l1 = random.randint(1, 29)
                    with open('languaged.json') as lang_strings:
                        data = json.load(lang_strings)
                        languagesd = data[str(l1)]
                    translatedText = translator.translate(originalText, dest=languagesd)
                    print(translatedText.text)

                translatedText2 = translator.translate(translatedText.text, dest='en')
                await message.channel.send(translatedText2.text)

client = MyClient()
client.run('Discord_bot_token')
