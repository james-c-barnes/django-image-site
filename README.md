# django-image-site

## Usage Notes

## Development Notes
### IP Address Notes
+ Everytime a new EC2 instance is started, a new ip is created.
+ Get IPv4 Public IP from instance Description and replace the ip with the older ones shown below.

#### Where New IP Address is needed
+ Putty Host Name field -- save new ip address
+ Django mysite/settings.py in ALLOWED_HOSTS. Otherwise, Bad Request (400) errors occur
+ Browser calls to ip address

### Start Site
+ Putty to EC2 host @ 54.90.102.31 (need pem file)
+ Launch django
```bash
    $ cd /opt/projects/django-image-site
    $ source env/bin/activate (note '(env)' on command line)
    $ python manage.py runserver 0.0.0.0:8000
```
+ Browser to http://54.90.102.31:8000/v1/image

### Launch Django shell
+ Putty to EC2 host (as above)
```bash
$ python manage.py shell
>>> from images.models import ServiceImage
>>> bird = ServiceImage.objects.get(name='Dodo bird')
>>> bird.image.name
u'Dodo.3.jpg'
>>> bird.image.path
u'/opt/projects/django-image-site/saved_images/Dodo.3.jpg'
```

### Rebuild Site
```bash
$ rm db.sqlite3
$ rm -rf images/migrations
$ python manage.py makemigrations images
$ python manage.py migrate
$ python manage.py createsuperuser
Username: <admin user>
Email address: <admin email>
Password: <admin password>
# browser to admin using above credentials
http://54.90.102.31:8000/admin
Create new user: tester01 with password: working01 (for running tests)
Give tester01 user permission to all 3 images selections
```

### HTTP Test
```bash
$ pip install httpie
$ http http://54.90.102.31:8000/v1/image/?format=json

HTTP/1.0 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Date: Sat, 17 Dec 2016 19:50:06 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

[
    {
        "created_date": "2016-12-17T19:34:42Z",
        "height": 151,
        "id": 2,
        "image": "Dodo.3.jpg",
        "modified_date": "2016-12-17T19:34:59.071328Z",
        "name": "Dodo bird",
        "size": 20819,
        "width": 143
    }
]

$ http http://54.90.102.31:8000/v1/image/2/?format=json

HTTP/1.0 200 OK
Allow: GET, PUT, DELETE, HEAD, OPTIONS
Content-Type: application/json
Date: Sat, 17 Dec 2016 19:52:49 GMT
Server: WSGIServer/0.1 Python/2.7.12
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "created_date": "2016-12-17T19:34:42Z",
    "height": 151,
    "id": 2,
    "image": "Dodo.3.jpg",
    "modified_date": "2016-12-17T19:34:59.071328Z",
    "name": "Dodo bird",
    "size": 20819,
    "width": 143
}

```

## Logging Notes

### Information Resource
https://www.loggly.com/docs/django-logs/

### Step 1 -- Configuration script
```bash

# copy the configuration script
$ curl -O https://www.loggly.com/install/configure-linux.sh

# run the configuration script
$ sudo bash configure-linux.sh -a SUBDOMAIN -u USERNAME

[ec2-user@ip-172-30-0-252 ~]$ sudo bash configure-linux.sh -a jamesbarnes -u james
Loggly account or subdomain: jamesbarnes
Username is set
Please enter Loggly Password:***********
INFO: Initiating Configure Loggly for Linux.
INFO: Operating system is Amazon AMI.
INFO: Checking if logs-01.loggly.com is reachable.
INFO: logs-01.loggly.com is reachable.
INFO: Checking if logs-01.loggly.com is reachable via 514 port. This may take some time.
INFO: logs-01.loggly.com is reachable via 514 port.
INFO: Checking if 'jamesbarnes' subdomain is valid.
INFO: https://jamesbarnes.loggly.com is valid and reachable.
INFO: Checking if Gen2 account.
INFO: It is a Gen2 account.
INFO: Checking if provided username and password is correct.
INFO: Username and password authorized successfully.
INFO: Authentication token not provided. Trying to retrieve it from https://jamesbarnes.loggly.com account.
INFO: Retrieved authentication token: e29a80c2-cf81-421a-bbae-ea0707e41d70
INFO: Checking if provided auth token is correct.
INFO: Authentication token validated successfully.
INFO: rsyslog is present as service.
INFO: Modified $MaxMessageSize to 64k in rsyslog.conf
INFO: Restarting the rsyslog service.
Shutting down system logger:                               [  OK  ]
Starting system logger:                                    [  OK  ]
INFO: Creating directory
mkdir: created directory ‘/var/spool/rsyslog’
INFO: Sending test message to Loggly.
INFO: Search URL: https://jamesbarnes.loggly.com/apiv2/search?q=syslog.appName%3ALOGGLYVERIFY%2013dAJl9CxVCr3vIWCscYkrwbOPnzaX3e
INFO: Verifying if the log made it to Loggly.
INFO: Verification # 1 of total 10.
INFO: Did not find the test log message in Loggly's search yet. Waiting for 30 secs.
INFO: Done waiting. Verifying again.
INFO: Verification # 2 of total 10.
SUCCESS: Verification logs successfully transferred to Loggly! You are now sending Linux system logs to Loggly.
```

### Step 2 -- Configure rsyslog
```
# note the replacing of TOKEN with the actual customer token
$ sudo vim /etc/rsyslog.d/21-django.conf
$ sudo service rsyslog restart
```

### Step 3 -- Configure Django
```
$ cd /opt/projects/django-image-site/mysite
# add LOGGING information to settings file
vim settings.py
```
