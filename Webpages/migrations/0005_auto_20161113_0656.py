# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-11-13 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Webpages', '0004_auto_20161101_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='barrage',
            field=models.FileField(null=True, upload_to='barrages/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
