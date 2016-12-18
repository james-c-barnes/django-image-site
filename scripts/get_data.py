import requests
from requests.auth import HTTPBasicAuth
import shutil

# http POST http://54.90.102.31:8000/v1/image/?format=json --auth tester01:working01

# get meta for id 2
print "\nView metadata about image with id 2."
r = requests.get(
    'http://54.90.102.31:8000/v1/image/2?format=json',
    auth=HTTPBasicAuth('tester01', 'working01')
)
meta = r.json()
filename = meta['image']

print "\nView image with id 2."
r = requests.get(
    'http://54.90.102.31:8000/v1/image/2/data?format=json',
    auth=HTTPBasicAuth('tester01', 'working01'),
    stream=True
)

# save the requested file
if r.status_code == 200:
    with open(filename, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
    print "{} saved.".format(filename)

print "\nOptional GET parameter: bbox=<x>,<y>,<w>,<h> to get a cutout of the image"
bbox = '10,10,10,10'
r = requests.get(
    'http://54.90.102.31:8000/v1/image/2/data?format=json&bbox={}'.format(bbox),
    auth=HTTPBasicAuth('tester01', 'working01'),
    stream=True
)

bbox_dashes = bbox.replace(',','-')
filename = '{}.{}'.format(bbox_dashes,filename)
if r.status_code == 200:
    with open(filename, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)
    print "{} saved.".format(filename)

