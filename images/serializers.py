from rest_framework import serializers
from images.models import Image
from django.db import models

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'name', 'image', 'width', 'height', 'size', 'created_date', 'modified_date')
