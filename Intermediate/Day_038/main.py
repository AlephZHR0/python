from auth import *
from datetime import datetime
import requests


Nutritionix_API_endpoint = "https://trackapi.nutritionix.com/v2"
HEADERS = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}
user_input = input("Wich exercises you did?\n")
parameters = {
    "query": user_input,
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age,
}
response = requests.post("{}/natural/exercise".format(Nutritionix_API_endpoint), headers=HEADERS, json=parameters)
content = response.json()

# Sheety configuration
sheety_endpoint = "https://api.sheety.co/"
projectName = "workoutsPython"
sheetName = "página1"
now = datetime.now()

#defining exercises
for exercise in content["exercises"]:
    data = {
        "página1": {
            "date": now.strftime("%d/%m/%Y"),
            "time": now.strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # Post information
    request = requests.post(url="{}{}/{}/{}".format(sheety_endpoint, USERNAME, projectName, sheetName), json=data, headers=AUTHORIZATION)
    print(request.text)


# # Receive information
# request = requests.get("{}{}/{}/{}".format(sheety_endpoint, USERNAME, projectName, sheetName))
# print(request.text)
# print(request.json())

###############--------- joao_39005@aluno.eseg.edu.br ---------###############