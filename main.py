import time
from xsense_api import XSenseApi
from mqtt import MqttClient
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

def fetch_and_publish_data():
    xsense_api = XSenseApi()
    xsense_api.initialize()
    
    states = xsense_api.fetch_data()

    mqtt_client = MqttClient(MQTT_BROKER, MQTT_PORT)
    mqtt_client.publish(states)

def main():
    while True:
        fetch_and_publish_data()
        time.sleep(30)

if __name__ == '__main__':
    main()
