# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='modified_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
