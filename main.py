import time
from mqtt_client import MQTTClient
from xsense_api import XSenseAPI

def monitor_and_send_status(xsense_api, mqtt_client):
    """Überwacht Geräte und sendet Statusänderungen per MQTT"""
    while True:
        for house in xsense_api.api.houses.values():
            for station in house.stations.values():
                status_info = xsense_api.get_device_status(station)
                
                # Wenn Statusänderungen vorliegen, an MQTT senden
                for status in status_info:
                    mqtt_client.send_message(status)

        # Alle 10 Sekunden nach Änderungen suchen (anpassbar)
        time.sleep(10)

def main():
    # MQTT-Client initialisieren
    mqtt_client = MQTTClient()
    
    # XSense API initialisieren und anmelden
    xsense_api = XSenseAPI()
    xsense_api.login()
    
    # Starten der Überwachung und des Sendens
    monitor_and_send_status(xsense_api, mqtt_client)

if __name__ == "__main__":
    main()
