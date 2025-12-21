import telebot
import os
import random

TOKEN = '8462297607:AAHY9vmDJ3meGAqmlu9DybKoXdyjtZ1SiXU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Команды:\n/meme\n/STARmeme")

@bot.message_handler(commands=['meme'])
def send_meme(message):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['starmeme'])
def send_starmeme(message):
    images2 = os.listdir('imagesstarvars')
    img_starname = random.choice(images2)
    with open(f'imagesstarvars/{img_starname}', 'rb') as f:
        bot.send_photo(message.chat.id, f)



@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)




bot.polling()
