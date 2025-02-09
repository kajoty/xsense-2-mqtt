from xsense import XSense
import config  # Importiere die Konfiguration

class XSenseAPI:
    def __init__(self):
        self.api = XSense()
        self.username = config.XSENSE_USERNAME
        self.password = config.XSENSE_PASSWORD
        self.previous_states = {}

    def login(self):
        """Login bei der XSense API"""
        self.api.init()
        self.api.login(self.username, self.password)
        self.api.load_all()

    def get_device_status(self, station):
        """Überprüfe den Status der Station und der Geräte"""
        status_info = []
        
        station_state = self.api.get_station_state(station)
        if station_state != self.previous_states.get(station.id):
            status_info.append(f"Station: {station.name}, Status: {station_state}")
            self.previous_states[station.id] = station_state
        
        for device in station.devices.values():
            device_state = self.api.get_state(device)
            if device_state != self.previous_states.get(device.id):
                status_info.append(f"Device: {device.name}, Status: {device_state}")
                self.previous_states[device.id] = device_state
        
        return status_info
