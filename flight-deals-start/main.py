#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager

sheet_data = data_manager.result

print(sheet_data)

# TODO: Check Flight Search API for cheapest flights from tomorrow to 6 months later for cities in Google Sheets

# TODO: If price is lower than the lowest price listed in the Google Sheet then send an SMS to my number in Twilio API

# TODO: The SMS should include the departure airport IATA code, destination airport IATA, departure and destination city, flight price and flight dates

for city in sheet_data.prices:
