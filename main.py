from config import token
from telebot import TeleBot
#aboba
bot = TeleBot(token)

@bot.message_handler(commands=['info'])
def send_message(message):
    bot.reply_to(message, 'Привет, меня зовут Владимир. Мне 14 лет')

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    bot.reply_to(message, 'What a photo!!!!!!!!')

bot.infinity_polling()


