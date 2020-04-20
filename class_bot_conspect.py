# Фигурка персонажа - алгоритмы двжений.

# функция "взять трехменую каринку и передвинуть вправо" 
# стоп, а как нам понять, что гг приблизился?
# Объект - поле. Например - дикт.

# Функция берет гг и меняет дикт.
# Иф изменения такие - действуй.

# То есть, можно в програмировании описать какую-то сущность, у коорой будут функции, присущие только ей. То есть их нельзя вызвать ,как прин СДЕЛАЙ, тлько ОБЪЕКТ сделай пожалуйста.



def test_function(arg):
	print(arg)


# Мы можем получть РЕЗУЛЬТАТ ВЫПОЛНЕНИЯ ДЕЙСТВИЯ, но у нас нет парметров, нет ДАННЫХ, или же атрибутов.

# Мы можем сказать что произошло действие, но с чем ии с кем - не понятно.




# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg



# class MyBot:
# 	name = "Bot"

# 	def say_hello():
# 		print("hello!")



# print(MyBot.name)
# MyBot.say_hello()




# class MyBot:
# 	name = "Bot"

# 	def say_hello():
# 		print(f"hello! {name}")

# print(MyBot.name)
# MyBot.say_hello()

# Мы обращаемся к ИНСТАНСУ а не к КЛАССУУ!!!



class MyBot:
	name = "Bot"

	def say_hello(self):
		print(f"hello! {self.name}")

MyBot().say_hello()


# print(MyBot)	
# print(MyBot())

# print(type(MyBot))	
# print(type(MyBot()))


# print(MyBot.name)
# MyBot.say_hello()



# СЕЛФ!!!

# то как с функцией, функция БЕЗ аргументов и скобочек, это объект СОВСЕМ другого типа.
# Т.е когда я говорю, что это чертеж и деталь, это БУКВАЛЬНО так - 

# def myfunc():
# 	pass

# вот эти вот две строчки это СОВСЕМ другой объект, чем

# myfunc()  - вот это, это команда, которая говорит - все кусочки з функции подгрузи в память, вычисли, произведи действия.
# То есть, компьютер буквально хранит и бумажку и болванку ,вытоенную по чертежу.


# Вот и с классаи то же самое.


# print(type(MyBot))	
# print(type(MyBot()))


# Окей, понятнО, то есть у нас идея такая, как и сфункцией, мы задаем ,собственно, тело, только вот
# раньше у нас в функции что бы мы не делали, мы могли обращаться ТОЛЬКО к тому что в ретурн.


# def test_func(arg):
# 	my_var = "Some value"
# 	return my_var,arg

# test_func.my_var


# Только так.
# test_func()


# Пока сложновато, да?

# Ничего, сделаем СРЕЗ ЗНАНИЙ!!!


class MyBot:
	name = "Bot"

	def say_hello(self):
		print(f"hello! {self.name}")

MyBot().say_hello()




# MyBot.say_hello()


# Приватные и __

# Области видимости! Отступы. Мы говорим - эта функция лежит тута!
# say_hello("egor")


# Что нам это дает?

# Возможность создавть КЛАСС, из из него рвзные ЭКЗЕМПЛЯРЫ.  То есть, наш Бот будет не кучей функций, а однм объектом.


# То есть у нас есть локализваная область видимости, где мы задаем данные и функции(методы) строго для нашего объекта.


# А могу я, например, создать класс пехотинец, но с разными парметрами? То есть, у меня ж что зомби что мужик в броне и с пулеметом имеют тело,
# верно?

# Можно я его буду расширять?




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


MyBot().send_message(message="Hello!")




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



MyBot().polling()


course_bot = MyBot()
course_bot.polling()
course_bot.send_message(message="Hi!")


Теперь выглядит знакомо, да?

class MyBot:
	_token = bot_token

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




Классы и инстансы

закрытые и открытые переменные

Задавать параметры через инит

Наследование

аргументы классов и объектов, геттеры и сеттеры




# функция и вызов функции

# класс и объект

