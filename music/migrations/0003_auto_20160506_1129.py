# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-06 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_auto_20160504_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='album_title',
            new_name='title',
        ),
    ]
