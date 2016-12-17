import requests
from requests.auth import HTTPBasicAuth

# http POST http://54.90.102.31:8000/v1/image/?format=json --auth tester01:working01

print "\nList metadata for stored images."
r = requests.get(
    'http://54.90.102.31:8000/v1/image/?format=json',
    auth=HTTPBasicAuth('tester01', 'working01')
)
print r.text

print "\nView metadata about image with id 2."
r = requests.get(
    'http://54.90.102.31:8000/v1/image/2/?format=json',
    auth=HTTPBasicAuth('tester01', 'working01')
)
print r.text
