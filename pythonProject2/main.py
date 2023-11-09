import requests
from twilio.rest import Client
account_sid = "AC6494178f136bb7a0db6ef4e5e2a7d41e"
auth_token = "10ad786642a942dc89e5323db86ee393"
parameters = {"lat": 39.954868,
              "lon": 66.312073,
              "appid": "cf622072964e7b3419a9c85b1c484d77",
              "exclude": "current,minutely,daily,"}
response = requests.get(url="https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
data = response.json()["hourly"][:12]
will_rain = False
for hour in data:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Remember to bring an ☔",
        from_="+14064681370",
        to="+998910114950"
    )
    print(message.status)
