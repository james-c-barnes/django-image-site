from django.contrib import admin

from .models import Image

class ImageAdmin(admin.ModelAdmin):
    readonly_fields=('height', 'width', 'size')

admin.site.register(Image, ImageAdmin)
