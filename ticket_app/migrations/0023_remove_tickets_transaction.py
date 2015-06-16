# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0022_auto_20150611_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='transaction',
        ),
    ]
