# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0010_auto_20150604_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='check_number',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
    ]
