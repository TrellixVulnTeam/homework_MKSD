# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-09 07:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('report_system', '0004_auto_20180209_1515'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='awatar',
            new_name='avatar',
        ),
    ]
