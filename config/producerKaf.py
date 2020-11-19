from time import sleep
from json import dumps
from kafka import KafkaProducer
import requests, json
producer = KafkaProducer(
    bootstrap_servers=['10.0.2.6:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8')
)

def get_data():
    api_key = "20245"
    base_url = "https://data.sensor.community/airrohr/v1/sensor/20245/"
    complete_url = base_url + api_key + "/"
    response = requests.get(base_url)
    return response.json()

def parse_data():
    response = get_data()
    sensorid = response[0]["sensor"]["id"]
    p1 = response[0]["sensordatavalues"][0]["value"]
    p2 = response[0]["sensordatavalues"][1]["value"]
    timestamp = response[0]["timestamp"]
    longitude = response[0]["location"]["longitude"]
    latitude = response[0]["location"]["latitude"]
    data = {"sensorid": sensorid, "longitude": longitude, "latitude": latitude, "P10": p1, "P2.5": p2, "timestamp": timestamp}
    return data

def send_data(data):
    producer.send('topic_test', value=data)
    sleep(0.5)

send_data(parse_data())