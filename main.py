import os
import requests
from twilio.rest import Client

OWM_ENPOINT = "https://api.openweathermap.org/data/2.5/forecast"

api_key = os.environ["OPENWEATHER_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
weather_params = {
    "lat": 11.556374,
    "lon": 104.928207,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENPOINT, params=weather_params)
response.raise_for_status() 

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
    body="It's going to rain today. Remember to bring an ☔",
    from_="+15076936046",
    to="+61405422327",
    )
    print(message.status)
else:
    client = Client(account_sid,auth_token)
    message = client.messages.create(
    body="It's not going to rain today just enjoy your day .Don't need to bring an umbrella ☂️",
    from_="+15076936046",
    to="+61405422327",
    )
    print(message.status)