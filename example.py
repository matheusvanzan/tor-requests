import requests
import tor_requests
import json


# Regular requests
print('Using requests...')
session = requests.session()
request = session.get('https://api.ipify.org?format=json')
response = json.loads(request.text)
ip = response['ip']
print('My Real IP:', ip)

# Tor requests
print('Using tor_requests...')
session = tor_requests.session()
request = session.get('https://api.ipify.org?format=json')
response = json.loads(request.text)
ip = response['ip']

print('My Hidden IP:', ip)