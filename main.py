import json
import xsense_api
from mqtt_client import MqttClient
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC, MQTT_USERNAME, MQTT_PASSWORD

def main():
    # Hole die XSense-Daten und speichere sie in einer Datei
    xsense_api.dump_xsense_data()

    # Lade die gespeicherten Daten aus der Datei
    with open("xsense_dump.json", "r") as file:
        data = json.load(file)

    # MQTT-Client initialisieren
    mqtt_client = MqttClient(MQTT_BROKER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD)

    # Sende jedes Gerät mit einem separaten Topic
    for device in data:
        topic = f"{MQTT_TOPIC}/{device.get('serial', 'unknown')}"
        payload = json.dumps(device)
        mqtt_client.publish(topic, payload)

if __name__ == "__main__":
    main()
