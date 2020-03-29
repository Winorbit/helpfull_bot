import requests

def get_ids_for_abrs(*args):
	requested_curr_ids = set([])
	res = requests.get("http://www.nbrb.by/api/exrates/currencies")

	currencies = res.json()
	for curr in currencies:
		if curr["Cur_Abbreviation"] in args:
			requested_curr_ids.add((curr["Cur_Code"]))

	return requested_curr_ids
	pass

def get_currencies_info(*args):
	message = "Курс на сегодня:"
	requested_ids = get_ids_for_abrs(*args)
	for x in requested_ids:
		curr_data = requests.get(f"http://www.nbrb.by/api/exrates/rates/{x}?parammode=1").json()

		scale = curr_data["Cur_Scale"]
		rate = curr_data["Cur_OfficialRate"]
		name = curr_data["Cur_Name"]

		message+=f"{rate} беларуских рублей за {scale} {name}\n"

	return message
	pass