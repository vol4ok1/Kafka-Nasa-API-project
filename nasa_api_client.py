from producer import send_message
from kafka import KafkaProducer
import requests
import json

API_KEY = input('Write your generated API KEY')
 
# Nasa API URL's
apod_url = f'https://api.nasa.gov/planetary/apod?api_key={API_KEY}'
insight_url = f'https://api.nasa.gov/insight_weather/?api_key={API_KEY}&feedtype=json&ver=1.0'
 
##parameters. Change date params for the day included, leave it/remove it for current day.

params= {
    'date':'2022-12-19',
    'hd':'True',
    'api_key':API_KEY
 }


def request_nasa_data():
    try:
        apod_request = requests.get(apod_url, params=params)
        insight_request = requests.get(insight_url, params=params)
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 200:
            # The request limit has been exceeded
            print("Request limit exceeded")
        else:
            # Some other HTTP error occurred
            raise err
    json_apod_data = json.loads(apod_request.text)
    json_insight_data = json.loads(insight_request.text)

    #send json_apod_data to the apod topic
    send_message(topic='api.analyst_data.apod_edvin', message=json_apod_data)
    
    #after ^ this one repeats itself and send insight to the other insight topic making 2 topic having each data
    send_message(topic='api.analyst_data.insight_edvin', message=json_insight_data)

    #Test data
    print(json_insight_data)
    print(json_apod_data)
 
 
request_nasa_data()
