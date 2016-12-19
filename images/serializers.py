from rest_framework import serializers
from images.models import ServiceImage
from django.db import models

class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ('id', 'name', 'image', 'width', 'height', 'size', 'filetype', 'created_date', 'modified_date')
