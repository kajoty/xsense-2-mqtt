from xsense import XSense
from xsense.utils import dump_environment
from config import XSENSE_USERNAME, XSENSE_PASSWORD, XSENSE_DUMP_PATH

def dump_xsense_data():
    api = XSense()
    api.init()
    api.login(XSENSE_USERNAME, XSENSE_PASSWORD)
    api.load_all()
    for _, h in api.houses.items():
        for _, s in h.stations.items():
            api.get_state(s)
    dump_environment(api, XSENSE_DUMP_PATH)
