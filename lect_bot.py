bot_token = "1104703407:AAF6o-H4LnOQv7TG49WSHIAEAgcw_wtsbyI"

# chat_id = 167233877


# https://api.telegram.org/bot1104703407:AAF6o-H4LnOQv7TG49WSHIAEAgcw_wtsbyI/getMe








# https://core.telegram.org/bots/api 

# https://api.telegram.org/bot1115299465:AAH0rlk64oIeu7TLhJTCSoGsGyYs79tapkU/getMe
# https://api.telegram.org/bot1115299465:AAH0rlk64oIeu7TLhJTCSoGsGyYs79tapkU/getUpdates



import requests  
# bot_info = requests.get("https://api.telegram.org/bot1104703407:AAF6o-H4LnOQv7TG49WSHIAEAgcw_wtsbyI/getMe")
bot_info = requests.get(f"https://api.telegram.org/bot{bot_token}/getMe")
print(bot_info.json())


chat_id = 167233877
res = requests.get(f"https://api.telegram.org/bot{bot_token}/sendMessage?text=hello&chat_id={chat_id}")
print(res.json())



# requests.post("https://api.telegram.org/bot1115299465:AAH0rlk64oIeu7TLhJTCSoGsGyYs79tapkU/sendMessage?text=hello&chat_id=167233877")
# requests.post("https://api.telegram.org/bot1115299465:AAH0rlk64oIeu7TLhJTCSoGsGyYs79tapkU/sendMessage", data={"text":"hello", "chat_id":167233877})
# requests.post("https://api.telegram.org/bot1115299465:AAH0rlk64oIeu7TLhJTCSoGsGyYs79tapkU/sendMessage", params={"text":"hello", "chat_id":167233877})






# root_address = "https://api.telegram.org/bot"
# sendMessage = f"{root_address}{bot_token}/sendMessage"
# # requests.post(sendMessage, data={"text":"hello", "chat_id":167233877})


# def send_message(chat_id, message):
# 	requests.post(sendMessage, data={"chat_id": chat_id, "text": message})

# send_message(167233877, "Hiii")


# def send_message(**kwargs):
# 	requests.post(sendMessage, data=kwargs)

# send_message(text="Hello world!", chat_id=167233877)


# def send_message(message="", chat_id=167233877):
# 	requests.post(sendMessage, data={"text":message, "chat_id":chat_id})

# send_message(chat_id=167233877)




# CHAT-iD ??


# get_updates_url = f"{root_address}{bot_token}/getUpdates"
# chat_id = requests.get(get_updates_url)
# print(chat_id)
# print(chat_id.json())

# print(chat_id.json()["result"][0]["message"]["chat"]["id"])

# def get_chat_id():
# 	get_updates_url = f"{root_address}{bot_token}/getUpdates"
# 	res = requests.get(get_updates_url)
# 	chat_id = res.json()["result"][0]["message"]["chat"]["id"]
# 	return chat_id

# chat_id = get_chat_id()


def get_chat_id(bot_token):
	get_updates_url = f"{root_address}{bot_token}/getUpdates"
	res = requests.get(get_updates_url)
	chat_id = res.json()["result"][0]["message"]["chat"]["id"]

	return chat_id

# chat_id = get_chat_id(bot_token)
# print(chat_id)







# ECHO-BOT 

# def send_message(message="", bot_token): 
# 	chat_id = get_chat_id(bot_token)
# 	requests.post(sendMessage, data={"text":message, "chat_id":chat_id})
# send_message(message = "Hi, variant 3!", bot_token)


# def send_message(bot_token, message="",): 
# 	chat_id = get_chat_id(bot_token)
# 	requests.post(sendMessage, data={"text":message, "chat_id":chat_id})

# # send_message(bot_token, message = "Hi, variant 3!")


# def get_updates(bot_token):
# 	get_updates_url = f"{root_address}{bot_token}/getUpdates"
# 	res = requests.get(get_updates_url)
# 	updates = res.json()["result"]

# 	return updates


# def echo_message(bot_token):
# 	updates = get_updates(bot_token)
# 	chat_id = updates[-1]["message"]["chat"]["id"]
# 	last_message = updates[-1]["message"]["text"]
# 	send_message(bot_token, message=last_message)

# echo_message(bot_token)


# bot_token = '724789546:AAGKGVe2C3opt27HOaXbw_KBvOlCAbZ9Tfg'
# tel_api_url = "https://api.telegram.org/bot{}/"

# methods = {'updates': 'GetUpdates'}



# def get_updates():
#     res = requests.get(tel_api_url.format(bot_token)+methods['updates'])
#     return res.json()



# def get_message_text(json_answer):
#     text_answer = json_answer['result'][-1]['message']['text']
#     chat_id = json_answer['result'][-1]['message']['chat']['id']
#     return text_answer, chat_id
#     pass

# print(get_message_text(get_updates()))


"""

Отличный видеоурок по пзработке телеграм-бота на питоне -  https://www.youtube.com/watch?v=iMBuy0INnHQ&list=WL&index=100&t=0s


# ДЗ 
- разделить скрипт на 3 фала - в одном лежат данные - token root_addres, send_message аддрес и т.д 
- в другом сами функции
- третий -для запуска, в нем нет логики ,только возможность вызова функций фалы с логикий с настройками из файла с переменными

В функциях, ходящих по аддресам добавить проверку статуса - если 200, то продолжаем выполнение ,нет - выводить сообщение о том ,что статус не из двухсотых

проверка длинны result в getUpdates - если список result длинной 1 или блоьше -то продложаем выполнение, нет - принтом выводим сообщение об этом


Задание со звезодчкой, хотя и не особо:
Используя функции для получения актуальных данных о курсе в виде текстового сообщения, отправлять это сообщение через бота

"""