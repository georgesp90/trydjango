# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20171001_1711'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='UserContacts',
        ),
    ]
