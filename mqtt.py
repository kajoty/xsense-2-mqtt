import paho.mqtt.client as mqtt
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_USERNAME, MQTT_PASSWORD

class MqttClient:
    def __init__(self, broker, port):
        self.client = mqtt.Client()
        self.client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        self.client.connect(broker, port, 60)

    def publish(self, device_data):
        for device, state in device_data.items():
            topic = f"{MQTT_TOPIC}/{device}"
            message = str(state) if state else "None"
            self.client.publish(topic, message)
            print(f"Published {message} to {topic}")
