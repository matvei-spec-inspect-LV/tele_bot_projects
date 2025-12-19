import telebot
from bot_logic import gen_pass
from bot_coin import coin_flip


# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['password'])
def send_hello(message):
    new_pass = gen_pass(20)
    bot.reply_to(message, f"твой пороль: {new_pass}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    result = coin_flip()
    bot.reply_to(message, f"Результат броска:{result}")

    

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
