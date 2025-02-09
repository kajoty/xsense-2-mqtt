import paho.mqtt.client as mqtt
import config  # Importiere die Konfiguration

class MQTTClient:
    def __init__(self):
        self.broker = config.MQTT_BROKER
        self.port = config.MQTT_PORT
        self.topic = config.MQTT_TOPIC
        self.username = config.MQTT_USERNAME
        self.password = config.MQTT_PASSWORD
        self.client = mqtt.Client()

        # Setup der Verbindung
        if self.username and self.password:
            self.client.username_pw_set(self.username, self.password)
        
        self.client.on_connect = self.on_connect
        self.client.connect(self.broker, self.port, 60)
        self.client.loop_start()

    def on_connect(self, client, userdata, flags, rc):
        """Callback-Funktion, die bei erfolgreicher Verbindung ausgeführt wird"""
        if rc == 0:
            print("Erfolgreich mit dem MQTT-Broker verbunden")
        else:
            print(f"Verbindung mit Broker fehlgeschlagen mit Code {rc}")

    def send_message(self, payload):
        """Nachricht an den Broker senden"""
        self.client.publish(self.topic, payload)
        print(f"Gesendet: {payload}")
