import requests
from datetime import datetime

APP_ID = "d81d5852"
API_KEY = "cd6788b71f120afd1c171c16c97e91e7"

today = datetime.now().strftime("%d/%m/%Y")
now = datetime.now().strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_query = {
    "query": input("Tell me which exercises you did: "),
}

response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_query)
result = response.json()
# print(result)

sheety_endpoint = "https://api.sheety.co/b68e93986ab164f6efff76d1b1361175/myWorkouts/workouts"

sheety_headers = {
    "Authorization": "Bearer YOUR_TOKEN"
}

for exercise in result["exercises"]:
    row_content = {
        "workout": {
            "date": today,
            "time": now,
            "exercise": exercise['name'].title(),
            "duration": exercise['duration_min'],
            "calories": exercise['nf_calories'],
        }
    }
    add_row = requests.post(url=sheety_endpoint, json=row_content, headers=sheety_headers)
    print(add_row.text)
