import requests
import json
from datetime import datetime

parameters = {
  "lat": 40.71,
  "lon": -74
 }
 

response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)

def jprint(obj):
  text = json.dumps(obj, sort_keys=True, indent=4)
  print(text)

pass_times = response.json()['response']
print('hey', pass_times)

risetimes = []

for v in pass_times:
  time = v['risetime']
  risetimes.append(time)

convertedtimes = []

for d in risetimes: 
  convert = datetime.fromtimestamp(d)
  convertedtimes.append(convert)
  print(convert)


jprint(risetimes)