import requests
from requests.auth import HTTPBasicAuth

# http POST http://54.90.102.31:8000/v1/image/?format=json --auth tester01:working01

r = requests.post(
    'http://54.90.102.31:8000/v1/image/?format=json',
    files={'image': open('/opt/projects/django-image-site/saved_images/Dodo.3.jpg')},
    data={'name': 'New Dodo'},
    auth=HTTPBasicAuth('tester01', 'working01')
)
print r.text
