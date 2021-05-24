import time

import requests
import schedule

def send_forecast():
    latitude = '49.6618'
    longitude = '32.0477'

    response = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&lang=uk&appid=${openweathermap-key}'.format(latitude, longitude))
    forecast = response.json()['daily'][0]['weather'][0]['description']

    if 'дощ' in forecast:
        text = "Сьогодні буде " + forecast + ' 😿'
    else:
        text = "Сьогодні буде " + forecast + ' 😺'
    requests.post('https://api.telegram.org/bot${telegram-bot-token}/sendMessage', {"chat_id": "${chat-ID}", "text": text})

schedule.every().day.at("09:24").do(send_forecast)

send_forecast()

while True:
    schedule.run_pending()
    time.sleep(1)

