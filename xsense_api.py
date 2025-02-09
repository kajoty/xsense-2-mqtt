from xsense import XSense
from config import XSENSE_USERNAME, XSENSE_PASSWORD

class XSenseApi:
    def __init__(self):
        self.api = XSense()

    def initialize(self):
        self.api.init()
        self.api.login(XSENSE_USERNAME, XSENSE_PASSWORD)

    def fetch_data(self):
        device_data = {}
        self.api.load_all()
        for _, house in self.api.houses.items():
            for _, station in house.stations.items():
                state = self.api.get_state(station)
                if state:
                    device_data[station.serial] = state.values if state.values else None
        return device_data
