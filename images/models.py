from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from django.utils import timezone

@python_2_unicode_compatible
class ServiceImage(models.Model):
    name = models.CharField(max_length=255, default='')
    image = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    width = models.PositiveIntegerField(default=0, editable=False)
    height = models.PositiveIntegerField(default=0, editable=False)
    size = models.PositiveIntegerField(default=0, editable=False)
    filetype = models.CharField(max_length=3, default='', editable=False)

    def __str__(self):
        return "{} -- {}".format(self.name, self.image.name)

    def save(self, *args, **kwargs):
        # add width and height
        self.width = self.image.width
        self.height = self.image.height
        self.size = self.image.size
        self.filetype = self.image.name[:3]
        if self.id:
            # existing instance -- update modified date
            self.modified_date = timezone.now()  
        super(ServiceImage, self).save(*args, **kwargs) 
