from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Image(models.Model):
    image = models.ImageField(upload_to='saved_images', default=None)
    created_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} -- {}.{}".format(self.name, self.filename, self.filetype)
