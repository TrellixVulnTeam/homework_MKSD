# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-08 12:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_system', '0002_article_bloginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64, null=True)),
                ('introduction', models.CharField(max_length=256, null=True)),
                ('posttime', models.CharField(max_length=32, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bloginfo',
            name='article',
        ),
        migrations.RemoveField(
            model_name='bloginfo',
            name='author',
        ),
        migrations.RemoveField(
            model_name='bloginfo',
            name='introduction',
        ),
        migrations.RemoveField(
            model_name='bloginfo',
            name='posttime',
        ),
        migrations.RemoveField(
            model_name='bloginfo',
            name='title',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user',
        ),
        migrations.AddField(
            model_name='bloginfo',
            name='btemplate',
            field=models.IntegerField(choices=[(1, 'spring'), (2, 'summer'), (3, 'autumn'), (4, 'winner')], default=1),
        ),
        migrations.AddField(
            model_name='user',
            name='awatar',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='blog',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='report_system.BlogInfo'),
        ),
        migrations.AddField(
            model_name='user',
            name='fans',
            field=models.ManyToManyField(to='report_system.User'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='article',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='pwd',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='rg_time',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='article',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='report_system.Article'),
        ),
        migrations.AddField(
            model_name='articleinfo',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='report_system.User'),
        ),
    ]
