# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-17 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='', max_length=128),
        ),
    ]
