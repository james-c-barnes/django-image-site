# django-image-site

## Usage Notes

## Development Notes
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
