import time

import requests
from datetime import datetime
import smtplib

MY_EMAIL = "bartek844@onet.pl"
MY_PASSWORD = "b0713841428"

MY_LAT = 51.107883
MY_LONG = 17.038538


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])


    # my position +- 5 degree from iss position

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,


    }
    ## wywalalo blad raise sslError rozwiazanie : verify = False = dziala
    response = requests.get(url = "https://api.sunrise-sunset.org/json?lat=51.107883&lng=17.038538",verify=False,params = parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return  True
while True:
    time.sleep((60))
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("bartek844@onet.pl")
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look UP \n\nThe ISS is above you"
        )





