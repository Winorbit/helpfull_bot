def test_function(arg):
	print(arg)


class MyBot:
	name = "Bot"

	def say_hello():
		print("hello!")


# say_hello()
# 
# print(MyBot.name)
# print(MyBot.say_hello())


# def print_args(name):
# 	size = 25
# 	print(name, size)

# print_args("KRatos")
# print_args("Enemy")

# print(type(print_args))
# print(type(print_args("Enemy")))


# class MyBot:
# 	name = "Bot"

# 	def say_hello():
# 		print(f"hello! {name}")

# print(MyBot.name)
# MyBot.say_hello()




class MyBot:
	name = "Bot"

	def say_hello(self):
		print(f"hello! {self.name}")

# MyBot().say_hello()


# print(MyBot)	
# print(MyBot())

# print(type(MyBot))	
# print(type(MyBot()))


# print(MyBot.name)
# MyBot.say_hello()


# def myfunc():
# 	pass



# print(MyBot.name)
# print(MyBot().name)





# def test_func(arg):
# 	my_var = "Some value"
# 	return my_var,arg

# test_func("s").my_var


# Только так.
# test_func()






class MyBot:
	name = "Bot"

	def say_hello(self):
		print(f"hello! {self.name}")




# MyBot().say_hello()
# MyBot(size=0.8).say_hello()







# def get_updates(bot_token):
# 	get_updates_url = f"{root_address}{bot_token}/getUpdates"
# 	res = requests.get(get_updates_url)
# 	updates = res.json()["result"]
# 	return updates
# 	pass

# def send_message(bot_token, message="",): 
# 	updates = get_updates(bot_token)
# 	chat_id = updates[-1]["message"]["chat"]["id"]
# 	requests.post(sendMessage, data={"text":message, "chat_id":chat_id})


# def extract_abrs_from_str(asc_string):
# 	return asc_string.replace(":", "").replace("курс","").replace(" ", "").split(",")


# def polling(bot_token):

# 	messages_count_start = 0

# 	while True:
# 		updates = get_updates(bot_token)
# 		messages_count = len(updates)

# 		if messages_count > messages_count_start:
# 			messages_count_start = messages_count
# 			last_message = updates[-1]["message"]["text"]

# 			if "курс:" in last_message:
# 				courses_abrs = extract_abrs_from_str(last_message)
# 				message = currencies.get_currencies_info(*courses_abrs)
# 				send_message(bot_token, message=message)

# polling(bot_token)



import requests  
import currencies
from settings import *

import settings



# def extract_abrs_from_str(asc_string):
# 	return asc_string.replace(":", "").replace("курс","").replace(" ", "").split(",")



# class MyBot:
# 	token = bot_token

# 	def get_updates(self):
# 		# ПОЧЕМУ БЕЗ АРГУМЕНТОВ
# 		get_updates_url = f"{root_address}{self.token}/getUpdates"
# 		res = requests.get(get_updates_url)
# 		updates = res.json()["result"]
# 		return updates
# 		pass

# 	def send_message(self, message=""): 
# 		# И ТУТ БЕЗ АРГУМЕНТОВ
# 		updates = self.get_updates()
# 		chat_id = updates[-1]["message"]["chat"]["id"]
# 		requests.post(sendMessage, data={"text":message, "chat_id":chat_id})


# MyBot().send_message(message="Hello!")




def extract_abrs_from_str(asc_string):
	return asc_string.replace(":", "").replace("курс","").replace(" ", "").split(",")



class MyBot:
	token = bot_token

	def get_updates(self):
		# ПОЧЕМУ БЕЗ АРГУМЕНТОВ
		get_updates_url = f"{root_address}{self.token}/getUpdates"
		res = requests.get(get_updates_url)
		updates = res.json()["result"]
		return updates
		pass

	def send_message(self, message=""): 
		# И ТУТ БЕЗ АРГУМЕНТОВ
		updates = self.get_updates()
		chat_id = updates[-1]["message"]["chat"]["id"]
		requests.post(sendMessage, data={"text":message, "chat_id":chat_id})



	def polling(self):

		messages_count_start = 0

		while True:
			updates = self.get_updates()
			messages_count = len(updates)

			if messages_count > messages_count_start:
				messages_count_start = messages_count
				last_message = updates[-1]["message"]["text"]

				if "курс:" in last_message:
					courses_abrs = extract_abrs_from_str(last_message)
					message = currencies.get_currencies_info(*courses_abrs)
					self.send_message(message=message)



# MyBot().polling()



course_bot.polling()
course_bot.send_message(message="Hi!")




# Классы и инстансы

# закрытые и открытые переменные

# Задавать параметры через инит

# Наследование

# аргументы классов и объектов, геттеры и сеттеры




# функция и вызов функции

# класс и объект

