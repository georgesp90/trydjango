# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-05 01:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_usercontacts_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercontacts',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='usercontacts',
            old_name='Phone',
            new_name='phone',
        ),
        migrations.AddField(
            model_name='usercontacts',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]