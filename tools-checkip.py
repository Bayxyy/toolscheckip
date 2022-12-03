import socket
import requests
import pprint
import json

print('''┌─────────────────────────────────────────────┐
│          IP CHECKER v1.0 By Bayxyy          │
├─────────────────────────────────────────────┤
│                    v1.0:                    │
│          [+] Using Python 3.11              │
│          [+] Optimization                   │
│          [+] Responsive for all Website     │
├─────────────────────────────────────────────┤
│ Link: https://github.com/Bayxyy/toolscheckip│
└─────────────────────────────────────────────┘''')

hostname = input('Masukan Domain Website : ')
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
        pprint.pprint(str(k) + ' : ' + str(v))
