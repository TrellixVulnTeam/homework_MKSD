# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-13 09:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
    ]
