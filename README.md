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
>>> from images.models import Image
>>> bird = Image.objects.get(name='Dodo bird')
>>> bird.image.name
u'Dodo.3.jpg'
>>> bird.image.path
u'/opt/projects/django-image-site/saved_images/Dodo.3.jpg'
```

### Build Site
```bash
$ python manage.py migrate
$ python manage.py createsuperuser
Username: <admin user>
Email address: <admin email>
Password: <admin password>
```
