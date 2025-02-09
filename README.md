
this Script uses the library found here:

https://pypi.org/project/python-xsense/

the github repo is here:
https://github.com/theosnel/python-xsense


```
sudo -i
```
## make virtual enviroment

```
python3 -m venv myenv
```

# activate

```
source myenv/bin/activate
```

# install python-xsense & aiohttp

```
pip install -r requirements.txt
```

```
pip install aiohttp
```

# create python file

```
nano sync-xsense.py
```

## paste code (change username (mailadresse) & password)


``` 
from xsense import XSense
from xsense.utils import dump_environment
 api = XSense()
api.init()
api.login(username, password)
api.load_all()
for _, h in api.houses.items():
     for _, s in h.stations.items():
         api.get_state(s)

dump_environment(api)
```



## save file

[CTRL] x -> y -> Enter

# start file

```
python3 sync-xsense.py >> daten.txt
```
# start process.py (change in file broker IP + Port)

```
python3 process.py
```