import json
import re
import paho.mqtt.client as mqtt

# Der MQTT-Broker und Port
BROKER_IP = "192.168.178.101"
BROKER_PORT = 1884

# Funktion zum Laden der Datei und Umwandeln in JSON
def load_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Stelle sicher, >        content = file.read()
    return content

# Funktion zum Parsen der Textdatei und Erstellen eines JSON-Objekts
def parse_data_to_json(data):
    devices = []

    # Regulärer Ausdruck zum Extrahieren von Gerätedaten
    device_pattern = re.compile(r"([A-Za-z0-9\s]+) \((.*?)\):\n\s*serial\s*>

    for match in device_pattern.finditer(data):
        device_name = match.group(1)
        device_type = match.group(2)
        serial = match.group(3)
        online = match.group(4).lower() == 'yes'
        values_str = match.group(5)