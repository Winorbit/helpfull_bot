import requests


# requests.get("http://www.nbrb.by/api/exrates/currencies")

# res = requests.get("http://www.nbrb.by/api/exrates/currencies")
# print(type(res.json()))



# curr_abr = ("USD", "RUB", "EUR")

# requested_curr_ids = []
# currencies = res.json()
# for curr in currencies:
# 	if curr["Cur_Abbreviation"] in curr_abr:
# 		print(curr["Cur_Code"])



# requested_curr_ids = set([])
# currencies = res.json()
# for curr in currencies:
# 	if curr["Cur_Abbreviation"] in curr_abr:
# 		requested_curr_ids.add((curr["Cur_Code"]))

# print(requested_curr_ids)


def get_ids_for_abrs(curr_abrs):
	requested_curr_ids = set([])
	
	res = requests.get("http://www.nbrb.by/api/exrates/currencies")
	currencies = res.json()

	for curr in currencies:
		if curr["Cur_Abbreviation"] in curr_abrs:
			requested_curr_ids.add((curr["Cur_Code"]))

	return requested_curr_ids
	pass



requested_ids = get_ids_for_abrs(("USD", "RUB", "EUR"))

mydict = {"name" : "Egor", "age" : 21}
print(mydict)
mydict["city"] = "Minsk"
print(mydict)





# print(requested_ids)



# curency_info = requests.get("http://www.nbrb.by/api/exrates/rates/643?parammode=1").json()

# print(curency_info)
# # print(type(curency_info))

# curr_data = {'Cur_ID': 298, 
# 'Date': '2020-03-16T00:00:00', 
# 'Cur_Abbreviation': 'RUB', 
# 'Cur_Scale': 100, 
# 'Cur_Name': 'Российских рублей', 
# 'Cur_OfficialRate': 3.1958}

# scale = curr_data["Cur_Scale"]
# rate = curr_data["Cur_OfficialRate"]
# name = curr_data["Cur_Name"]

# print(f"Курс на сегодня: {rate} беларуских рублей за {scale} {name}")






def get_currencies_info():


	requested_ids = get_ids_for_abrs(("USD", "RUB", "EUR"))
                  # requested_ids =      648    773    875

	for x in requested_ids:
		curr_data = requests.get(f"http://www.nbrb.by/api/exrates/rates/{x}?parammode=1").json()

		scale = curr_data["Cur_Scale"]
		rate = curr_data["Cur_OfficialRate"]
		name = curr_data["Cur_Name"]

		print(f"Курс на сегодня: {rate} беларуских рублей за {scale} {name}")

# get_currencies_info()





def get_currencies_info():
	message = "Курс на сегодня:"

	requested_ids = get_ids_for_abrs(("USD", "RUB", "EUR"))
	for x in requested_ids:
		curr_data = requests.get(f"http://www.nbrb.by/api/exrates/rates/{x}?parammode=1").json()

		scale = curr_data["Cur_Scale"]
		rate = curr_data["Cur_OfficialRate"]
		name = curr_data["Cur_Name"]

		message+=f"{rate} беларуских рублей за {scale} {name}\n"

	return message
	pass

curr_info = get_currencies_info()
print(curr_info)