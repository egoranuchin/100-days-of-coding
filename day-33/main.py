import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 44.786568
MY_LNG = 20.448921

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
# print(response)

longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

# if my position is within +-5 degrees to the position of ISS

iss_position = (latitude, longitude)

print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])



print(sunrise, sunset)

time_now = datetime.now()

print(time_now.hour)


def is_iss_near():
    is_near = False
    if MY_LAT-5 <= iss_position[0] <= MY_LAT+5 and MY_LNG+5 >= iss_position[1] >= MY_LNG - 5:
        is_near = True
    # print(is_near)
    return is_near


def is_it_dark():
    is_dark = False
    if (sunset + 1) < time_now.hour < (sunrise + 1):
        is_dark = True
    # print(is_dark)
    return is_dark

# if my lng+ltd is within 5 dgr with iss_position and time_now = :
# send email


def do_i_look_up():
    print(is_it_dark())
    print(is_iss_near())
    if is_iss_near() and is_it_dark():
        print("Look up")
    else:
        print("Don't look up")

while True:
    time.sleep(60)
    do_i_look_up()
