from django.contrib import admin

from .models import ServiceImage

class ServiceImageAdmin(admin.ModelAdmin):
    readonly_fields=('height', 'width', 'size')

admin.site.register(ServiceImage, ServiceImageAdmin)
