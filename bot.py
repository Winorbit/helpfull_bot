from settings import *
import telebot

# pip install pyTelegramBotAPI
# https://github.com/eternnoir/pyTelegramBotAPI

bot = telebot.TeleBot(bot_token)


# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")


# bot.polling()






# @bot.message_handler(commands=['hello'])
# def send_welcome(message):
# 	print(message.text)

# bot.polling()






from bot_utils import *

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if "курс:" in message.text:
		courses_abrs = extract_abrs_from_str(message.text)
		new_message = currencies.get_currencies_info(*courses_abrs)
		# send_message(bot_token, message=new_message)
		bot.send_message(message.chat.id, new_message)

bot.polling()

