import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

TOKEN = "gsrgrg44g4ssef"
USERNAME = "egoranuchin"

# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Writing Graph",
    "unit": "Lines",
    "type": "int",
    "color": "ichou",
}

headers = {
    "X-USER-TOKEN": TOKEN
}


# response = requests.post(url=create_graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many lines you wrote today? "),
}

response = requests.post(url=add_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)
