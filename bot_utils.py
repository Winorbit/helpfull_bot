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


def extract_abrs_from_str(asc_string):
	return asc_string.replace(":", "").replace("курс","").replace(" ", "").split(",")


