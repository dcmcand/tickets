# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0005_auto_20150527_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='library',
            field=models.CharField(default='Leb', max_length=3, choices=[(b'Leb', b'Lebanon'), (b'KPL', b'Kilton')]),
            preserve_default=False,
        ),
    ]
