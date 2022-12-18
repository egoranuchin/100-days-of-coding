import requests
import os
from twilio.rest import Client

# OpenWeatherMap creds:

api_key = os.environ.get("OMW_API_KEY")

# Twilio creds:

account_sid = os.environ.get("SID")
auth_token = os.environ.get("AUTH_TOKEN")


my_lat = 44.786568
my_lng = 20.448921

parameters = {
    "lat": my_lat,
    "lon": my_lng,
    "appid": api_key,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["weather"][0]["id"])

will_rain = False

if int(weather_data["weather"][0]["id"]) < 700:
    will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_='+14092543489',
        to='+381616441296'
    )
    # If weather ID is < 700: bring umbrella
    print(message.status)