# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-25 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20160515_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(max_length=100),
        ),
    ]