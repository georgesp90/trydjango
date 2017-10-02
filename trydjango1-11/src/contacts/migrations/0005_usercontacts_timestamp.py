# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20171001_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercontacts',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 1, 23, 44, 52, 493343, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
