import socket
import requests
import pprint
import json

print('THIS SCRIPT CREATED BY Bayxyy')
print('the function of this script is to find the ip address of a website')

hostname = input('Masukan Domain Website : ')
ip_address = socket.gethostbyname(hostname)

request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
geolocation = response.content.decode()
geolocation = geolocation.split("(")[1].strip(")")
geolocation = json.loads(geolocation)
for k,v in geolocation.items():
        pprint.pprint(str(k) + ' : ' + str(v))