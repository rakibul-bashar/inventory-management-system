# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 06:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims_app', '0007_auto_20170411_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockin',
            name='created_date',
            field=models.DateTimeField(),
        ),
    ]
