# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-12 07:09
from __future__ import unicode_literals

import contacts.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_usercontacts_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercontacts',
            name='time_zone',
            field=models.CharField(default=django.utils.timezone.now, max_length=120, validators=[contacts.validators.validate_timezone]),
            preserve_default=False,
        ),
    ]