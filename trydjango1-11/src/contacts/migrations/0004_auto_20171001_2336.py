# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20171001_1717'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usercontacts',
            options={'verbose_name': 'User Contact', 'verbose_name_plural': 'User Contacts'},
        ),
        migrations.AlterField(
            model_name='usercontacts',
            name='Phone',
            field=models.CharField(max_length=9, null=True),
        ),
    ]
