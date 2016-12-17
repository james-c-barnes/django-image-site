# django-image-site

## Development Notes
### Start Site
+ Putty to EC2 host @ 54.90.102.31 (need pem file)
+ Launch django
```bash
    cd to /opt/projects/django-image-site
    source env/bin/activate (note '(env)' on command line)
    python manage.py runserver 0.0.0.0:8000
```
+ Browser to http://54.90.102.31:8000/v1/image
