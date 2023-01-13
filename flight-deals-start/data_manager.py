from pprint import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass

sheety_get_endpoint = "https://api.sheety.co/b68e93986ab164f6efff76d1b1361175/flightDeals/prices"

table_data_raw = requests.get(url=sheety_get_endpoint)
table_data = table_data_raw.json()

# pprint(table_data)

# print(table_data["prices"])

sheety_put_endpoint = "https://api.sheety.co/b68e93986ab164f6efff76d1b1361175/flightDeals/prices/1"




change_table_data = requests.put(url=sheety_put_endpoint, json=)