import requests  
import currencies
from settings import *

def get_chat_id(bot_token):
	get_updates_url = f"{root_address}{bot_token}/getUpdates"
	res = requests.get(get_updates_url)
	chat_id = res.json()["result"][0]["message"]["chat"]["id"]
	return chat_id


def get_updates(bot_token):
	get_updates_url = f"{root_address}{bot_token}/getUpdates"
	res = requests.get(get_updates_url)
	updates = res.json()["result"]
	return updates

def send_message(bot_token, message="",): 
	updates = get_updates(bot_token)
	chat_id = updates[-1]["message"]["chat"]["id"]
	requests.post(sendMessage, data={"text":message, "chat_id":chat_id})

def echo_message(bot_token):
	updates = get_updates(bot_token)
	chat_id = updates[-1]["message"]["chat"]["id"]
	last_message = updates[-1]["message"]["text"]
	send_message(bot_token, message=last_message)


## POOLING 1 VARIANT 
def polling(bot_token):

	messages_count_start = 0

	while True:
		updates = get_updates(bot_token)
		messages_count = len(updates)

# polling(bot_token)


## POOLING 2 VARIANT 
def polling(bot_token):
	messages_count_start = 0

	while True:
		updates = get_updates(bot_token)
		messages_count = len(updates)

		if messages_count > messages_count_start:
			messages_count_start = messages_count
			last_message = updates[-1]["message"]["text"]
			print(last_message)


###  POOLING VARIANT 3
def polling(bot_token):

	messages_count_start = 0

	while True:
		updates = get_updates(bot_token)
		messages_count = len(updates)

		if messages_count > messages_count_start:
			messages_count_start = messages_count
			last_message = updates[-1]["message"]["text"]
			if last_message == "echo":
				send_message(bot_token, message=last_message)







# "курс: USD, UAH, GBR"

# def extract_abrs_from_str(asc_string):
# 	print(asc_string.split(","))
# extract_abrs_from_str("курс: USD, UAH, GBR")


# def extract_abrs_from_str(asc_string):
# 	return asc_string.replace(":", "").replace("курс","").split(",")

# cleared_message = extract_abrs_from_str("курс: USD, UAH, GBR")

# curr_info = currencies.get_currencies_info(cleared_message)
# print(curr_info)





#ПРОБЛЕМА С ПРОБЕЛОМ
def extract_abrs_from_str(asc_string):
	return asc_string.replace(":", "").replace("курс","").replace(" ", "").split(",")

# cleared_message = extract_abrs_from_str("курс: USD, UAH, GBR")
# print(cleared_message)

# curr_info = currencies.get_currencies_info(*cleared_message)
# print(curr_info)


####  POOLING VARIANT 4
def polling(bot_token):

	messages_count_start = 0

	while True:
		updates = get_updates(bot_token)
		messages_count = len(updates)

		if messages_count > messages_count_start:
			messages_count_start = messages_count
			last_message = updates[-1]["message"]["text"]
			if last_message == "echo":
				send_message(bot_token, message=last_message)
			if "курс:" in last_message:
				courses_abrs = extract_abrs_from_str(last_message)
				message = currencies.get_currencies_info(*courses_abrs)
				send_message(bot_token, message=message)



polling(bot_token)






# import telebot

# bot = telebot.TeleBot(bot_token)

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")


# bot.polling()


