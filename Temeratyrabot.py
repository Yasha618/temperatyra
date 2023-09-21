from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from urllib.request import urlopen
from bs4 import BeautifulSoup
import telebot

from urllib.request import urlopen
from bs4 import BeautifulSoup



TOKEN = "5950094793:AAFZkmLi5s0ijBxJA67ifoKqpfYq3QZD8t4"
bot = telebot.TeleBot(token=TOKEN)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if message.text == "Привет":
      bot.send_message(message.from_user.id, msg)
  elif message.text.lower() == "в боинге":
        url = "http://10.13.2.9/"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()    # rip it out
        text = soup.get_text()
        text = text.replace('Visitor counter: 286', '')
        text = text.replace('Visitor counter: 287', '')
        text = text.replace('Visitor counter: 288', '')
        text = text.replace('Visitor counter: 2', '')
        text = text.replace('Visitor counter: 3', '')
        text = text.replace('Visitor counter: 4', '')
        text = text.replace('Visitor counter: 5', '')
        text = text.replace('Visitor counter: 6', '')
        text = text.replace('Visitor counter: 7', '')
        text = text.replace('Visitor counter: 8', '')
        text = text.replace('Visitor counter: 9', '')
        text = text.replace('Visitor counter: 10', '')
        text = text.replace('Visitor counter: 11', '')
        text = text.replace('Visitor counter: 12', '')
        text = text.replace('Visitor counter: 13', '')
        text = text.replace('Visitor counter: 14', '')
        text = text.replace('Visitor counter: 15', '')
        text = text.replace('Visitor counter: 16', '')
        text = text.replace('Visitor counter: 17', '')
        text = text.replace('Visitor counter: 18', '')
        text = text.replace('Visitor counter: 19', '')
        text = text.replace('Visitor counter: 20', '')
        text = text.replace('Visitor counter: 21', '')
        text = text.replace('Visitor counter: 22', '')
        text = text.replace('Visitor counter: 23', '')
        text = text.replace('Visitor counter: 24', '')
        text = text.replace('Visitor counter: 25', '')
        text = text.replace('Visitor counter: 26', '')
        text = text.replace('Visitor counter: 27', '')
        text = text.replace('Visitor counter: 28', '')
        text = text.replace('Visitor counter: 29', '')
        text = text.replace('Visitor counter: 30', '')
        text = text.replace('Visitor counter: 16', '')
        text = text.replace('Visitor counter: 17', '')
        text = text.replace('Visitor counter: 289', '')
        text = text.replace('Visitor counter: 290', '')
        text = text.replace('Visitor counter: 291', '')
        text = text.replace('Visitor counter: 292', '')
        text = text.replace('Visitor counter: 293', '')
        text = text.replace('Visitor counter: 294', '')
        text = text.replace('Visitor counter: 295', '')
        text = text.replace('Visitor counter: 296', '')
        text = text.replace('Visitor counter: 297', '')
        text = text.replace('Visitor counter: 298', '')
        text = text.replace('Visitor counter: 299', '')
        text = text.replace('Visitor counter: 300', '')
        text = text.replace('Visitor counter: 301', '')
        text = text.replace('Visitor counter: 302', '')
        text = text.replace('Socket 1', '')
        text = text.replace('Main', 'В Боинге')
        text = text.replace('Socket 2', '')
        text = text.replace('S0', 'Датчик на стене')
        text = text.replace('S1', 'Первый правый кондиционер')
        text = text.replace('S4', 'Второй-средний кондиционер')
        text = text.replace('S5', 'Третий левый кондиционер')
        text = text.replace('TE_MONITOR V2 v1.85 2014', '')
        text = text.replace('TE_MONITOR V2', '')
        text = text.replace('Setup', '')
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        bot.send_message(-825895148, text)
        bot.send_message(message.from_user.id, text)
  elif message.text.lower() == "В подвале":
        url = "http://10.13.2.11/"
        html = urlopen(url).read()
        soup = BeautifulSoup(html, features="html.parser")
        for script in soup(["script", "style"]):
            script.extract()
        text = soup.get_text()
        text = text.replace('Main', 'В подвале 17с2')
        text = text.replace('S0', 'Левый кондиционер')
        text = text.replace('S4', 'Правый кондиционер')
        text = text.replace('Socket 1', '')
        text = text.replace('Socket 2', '')
        text = text.replace('Visitor counter: 1', '')
        text = text.replace('Visitor counter: 2', '')
        text = text.replace('Visitor counter: 3', '')
        text = text.replace('Visitor counter: 4', '')
        text = text.replace('Visitor counter: 5', '')
        text = text.replace('Visitor counter: 6', '')
        text = text.replace('Visitor counter: 7', '')
        text = text.replace('Visitor counter: 8', '')
        text = text.replace('Visitor counter: 9', '')
        text = text.replace('Visitor counter: 10', '')
        text = text.replace('Visitor counter: 11', '')
        text = text.replace('Visitor counter: 12', '')
        text = text.replace('Visitor counter: 13', '')
        text = text.replace('Visitor counter: 14', '')
        text = text.replace('Visitor counter: 15', '')
        text = text.replace('Visitor counter: 16', '')
        text = text.replace('Visitor counter: 17', '')
        text = text.replace('TE_MONITOR V2 v1.85 2014', '')
        text = text.replace('TE_MONITOR V2', '')
        text = text.replace('Setup', '')
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text12 = '\n'.join(chunk for chunk in chunks if chunk)
        bot.send_message(-825895148, text12)
        bot.send_message(message.from_user.id, text12)



bot.polling(none_stop=True, interval=0)
