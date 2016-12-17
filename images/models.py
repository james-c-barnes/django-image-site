from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Image(models.Model):
    name = models.CharField(max_length=128, default='')
    filename = models.CharField(max_length=128)
    filetype = models.CharField(max_length=128)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    created_date = models.DateTimeField('date created')
    updated_date = models.DateTimeField('date published')

    def __str__(self):
        return "{} -- {}.{}".format(self.name, self.filename, self.filetype)
