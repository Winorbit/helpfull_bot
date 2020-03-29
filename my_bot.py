from bot_utils import *
from settings import *


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