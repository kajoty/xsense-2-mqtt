
https://pypi.org/project/python-xsense/

sudo -i

## made virtual enviroment

python3 -m venv myenv

# activate
source myenv/bin/activate

# install python-xsense & aiohttp

pip install python-xsense

pip install aiohttp

# create python file

nano sync-xsense.py

# paste code (change username (mailadresse) & password)

import xsense
from xsense import XSense
from xsense.utils import dump_environment
api = XSense()
api.init()
api.login("username", "password")
api.load_all()
for _, h in api.houses.items():
for _, s in h.stations.items():
api.get_state(s)


dump_environment(api)

# save file

## start file
python3 sync-xsense.py


