import requests
from datetime import datetime
import smtplib
from time import sleep
MY_EMAIL = "test@example.com"
MY_PASSWORD = "passwordexample123"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

def is_in_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True
        

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    
    if time_now.hour >= sunset or time_now.hour <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark

while True:
    if is_in_range() and is_night():
        conection = smtplib.SMTP("smtp.gmail.com", port=587)
        conection.login(user=MY_EMAIL, password=MY_PASSWORD)
        conection.sendmail(from_addr=MY_EMAIL, to_addrs="another_mail@example.com", msg="Subject: ISS NEARBY\n\nYo, look up, ISS is passing above you")
    sleep(60)
# Then send me an email to tell me to look up.

# BONUS: run the code every 60 seconds.
