# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-04 03:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('作业一', '0003_auto_20180203_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinf',
            fields=[
                ('uid', models.BigAutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='password',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='users',
            name='age',
        ),
        migrations.RemoveField(
            model_name='users',
            name='nw',
        ),
        migrations.RemoveField(
            model_name='users',
            name='ug',
        ),
        migrations.RemoveField(
            model_name='users',
            name='usernamenew',
        ),
    ]
