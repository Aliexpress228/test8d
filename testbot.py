import telebot
#from fuzzywuzzy import fuzz
import requests

TOKEN = '1473701302:AAHdrETRWTGIyVvhJBXlIg3oqFvYmH3uxys'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'создан для теста платформы henkaku')
@bot.message_handler(content_types=['text'])
def choose(message):
    bot.send_message(message.chat.id, 'тест платформы хероку')
bot.polling(none_stop=True)

