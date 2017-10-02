# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='Phone',
            field=models.CharField(max_length=9, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='contacts',
            name='location',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
    ]
