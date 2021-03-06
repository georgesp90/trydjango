# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-10 01:00
from __future__ import unicode_literals

import contacts.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20171005_0118'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontacts',
            name='time_zone',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[contacts.validators.validate_timezone]),
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='phone',
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
