import requests
from auth import *
pixela_endpoint = "https://pixe.la/v1/users"
# Creating user
parameters = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
request = requests.post(url="{}".format(pixela_endpoint), json=parameters)
# Creating a graph
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_id = "programingtrack"
parameters = {
    "id": graph_id,
    "name": "Programing time tracker",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai",
    "timezone": "America/Sao_Paulo"
}
request = requests.post("{}/{}/graphs".format(pixela_endpoint, USER_NAME), json=parameters, headers=headers)
# Creating a pixel
pixel_creation_endpoint = "{}/{}/graphs/{}".format(pixela_endpoint, USER_NAME, graph_id)
pixel_data = {
    "date": "20230220",
    "quantity": "10"
}
request = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# Updating a pixel
request = requests.put(url="{}/{}/graphs/{}/{}".format(pixela_endpoint, USER_NAME, graph_id, "20230221"), json={"quantity": "0"}, headers=headers)
# Deleting graph
request = requests.delete(url="{}/{}/graphs/{}".format(pixela_endpoint, USER_NAME, graph_id), headers=headers)
# Delete user
request = requests.delete(url="{}/{}".format(pixela_endpoint, USER_NAME), headers=headers)