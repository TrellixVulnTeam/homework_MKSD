# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-06 02:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('作业一', '0007_auto_20180205_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='作业一.UserBoy')),
                ('girl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='作业一.UserGirl')),
            ],
        ),
        migrations.DeleteModel(
            name='Userinf',
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
