import json
import re
import paho.mqtt.client as mqtt

# Der MQTT-Broker und Port
BROKER_IP = "192.168.178.101"
BROKER_PORT = 1884

# Funktion zum Laden der Datei und Umwandeln in JSON
def load_data_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:  # Stelle sicher, dass die Datei mit UTF-8 codiert eingelesen wird
        content = file.read()
    return content

# Funktion zum Parsen der Textdatei und Erstellen eines JSON-Objekts
def parse_data_to_json(data):
    devices = []

    # Regulärer Ausdruck zum Extrahieren von Gerätedaten
    device_pattern = re.compile(r"([A-Za-z0-9\s]+) \((.*?)\):\n\s*serial\s*:\s*(\S+)\n\s*online\s*:\s*(\S+)\n\s*values\s*:\s*\{(.*?)\}", re.DOTALL)

    for match in device_pattern.finditer(data):
        device_name = match.group(1)
        device_type = match.group(2)
        serial = match.group(3)
        online = match.group(4).lower() == 'yes'
        values_str = match.group(5)

        # Werte extrahieren und in ein Dictionary umwandeln
        values = {}
        for line in values_str.split('\n'):
            if line.strip():  # Leere Zeilen überspringen
                key_value = line.split(':')
                if len(key_value) == 2:
                    key = key_value[0].strip()
                    value = key_value[1].strip()
                    # Versuchen, den Wert in das passende Format zu konvertieren
                    try:
                        values[key] = eval(value)  # Wandelt Strings wie 'True' oder '3' in die richtigen Datentypen um
                    except:
                        values[key] = value

        # Gerätedaten zu einer Liste hinzufügen
        devices.append({
            "deviceName": device_name,
            "serial": serial,
            "online": online,
            "values": values
        })

    return {"devices": devices}
# Callback-Funktionen für MQTT-Verbindung
def on_connect(client, userdata, flags, rc):
    print(f"Verbunden mit Broker, Rückgabecode {rc}")
    # JSON-Daten an das definierte Topic senden
    client.publish("devices", json.dumps(json_data, ensure_ascii=False))  # ensure_ascii=False sorgt dafür, dass Umlaute korrekt übermittelt werden
    print(f"Gesendet an Topic 'devices':\n{json.dumps(json_data, ensure_ascii=False)}")
    # Verbindung nach dem Senden trennen
    client.disconnect()

def on_disconnect(client, userdata, rc):
    print(f"Verbindung getrennt mit Rückgabecode {rc}")

# MQTT-Client initialisieren
def send_data_to_mqtt(json_data):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect

    # Verbindung zum Broker herstellen
    client.connect(BROKER_IP, BROKER_PORT, 60)

    # MQTT-Client starten, um Nachrichten zu senden
    client.loop_forever()

# Der Pfad zur Datei
file_path = 'daten.txt'

# Daten aus der Datei laden
data = load_data_from_file(file_path)

# Daten in JSON umwandeln
json_data = parse_data_to_json(data)

# Überprüfen, ob die JSON-Daten korrekt erstellt wurden
if json_data:
    # JSON-Daten an den MQTT-Broker senden
    send_data_to_mqtt(json_data)
else:
    print("Fehler beim Umwandeln der Daten in JSON.")
