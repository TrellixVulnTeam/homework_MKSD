# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-03 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('作业一', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='usernamenew',
        ),
        migrations.AddField(
            model_name='users',
            name='nw',
            field=models.BooleanField(default=True),
        ),
    ]
