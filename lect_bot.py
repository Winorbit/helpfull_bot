import requests  
import currencies
from settings import *

def get_updates(bot_token):
	get_updates_url = f"{root_address}{bot_token}/getUpdates"
	res = requests.get(get_updates_url)
	updates = res.json()["result"]
	return updates
	pass

def send_message(bot_token, message="",): 
	updates = get_updates(bot_token)
	chat_id = updates[-1]["message"]["chat"]["id"]
	requests.post(sendMessage, data={"text":message, "chat_id":chat_id})

def echo_message(bot_token):
	updates = get_updates(bot_token)
	chat_id = updates[-1]["message"]["chat"]["id"]
	last_message = updates[-1]["message"]["text"]
	send_message(bot_token, message=last_message)


# POOLING 1 VARIANT 



# def polling(bot_token):
# 	while True:
# 		updates = get_updates(bot_token)
# 		messages_count = len(updates)
# 		print(messages_count)

# polling(bot_token)







# POOLING 2 VARIANT 
# def polling(bot_token):
# 	messages_count_start = 0

# 	while True:
# 		updates = get_updates(bot_token)
# 		messages_count = len(updates)

# 		if messages_count > messages_count_start:
# 			messages_count_start = messages_count
# 			last_message = updates[-1]["message"]["text"]
# 			print(last_message)


# polling(bot_token)


# ###  POOLING VARIANT 3
# def polling(bot_token):

# 	messages_count_start = 0

# 	while True:
# 		updates = get_updates(bot_token)
# 		messages_count = len(updates)

# 		if messages_count > messages_count_start:
# 			messages_count_start = messages_count
# 			last_message = updates[-1]["message"]["text"]
# 			# if last_message == "echo":
# 			# 	send_message(bot_token, message=last_message)

# 			send_message(bot_token, message=last_message)


# polling(bot_token)





# "курс: USD, UAH, GBR"


# print("курс: USD, UAH, GBR".split(","))

# def extract_abrs_from_str(asc_string):
# 	print(asc_string.split(","))

# extract_abrs_from_str("курс: USD, UAH, GBR")


# def extract_abrs_from_str(asc_string):
# 	return asc_string.replace(":", "").replace("курс","").split(",")



# cleared_message = extract_abrs_from_str("курс: USD, UAH, GBR")
# print(cleared_message)



# curr_info = currencies.get_currencies_info(cleared_message)
# print(curr_info)




# ПРОБЛЕМА С ПРОБЕЛОМ
def extract_abrs_from_str(asc_string):
	return asc_string.replace(":", "").replace("курс","").replace(" ", "").split(",")



# cleared_message = extract_abrs_from_str("курс: USD, UAH, GBR")
# # print(cleared_message)

# curr_info = currencies.get_currencies_info(*cleared_message)
# print(curr_info)


###  POOLING VARIANT 4
def polling(bot_token):

	messages_count_start = 0

	while True:
		updates = get_updates(bot_token)
		messages_count = len(updates)

		if messages_count > messages_count_start:
			messages_count_start = messages_count
			last_message = updates[-1]["message"]["text"]

			if "курс:" in last_message:
				courses_abrs = extract_abrs_from_str(last_message)
				message = currencies.get_currencies_info(*courses_abrs)
				send_message(bot_token, message=message)



polling(bot_token)




## WORK WITH LIBRIARY ###

# https://github.com/eternnoir/pyTelegramBotAPI
# pip install pyTelegramBotAPI



import telebot

bot = telebot.TeleBot(bot_token)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(commands=['hello'])
# def send_welcome(message):
# 	bot.send_message(message.chat.id, message.text)

# # @bot.message_handler(commands=['course'])
# # def send_welcome(message):
# # 	bot.send_message(message.chat.id, message.text)



@bot.message_handler()
def send_welcome(message):
	if "курс:" in message.text:
		courses_abrs = extract_abrs_from_str(message.text)
		courses_info = currencies.get_currencies_info(*courses_abrs)
		bot.send_message(message.chat.id, courses_info)

bot.polling()


