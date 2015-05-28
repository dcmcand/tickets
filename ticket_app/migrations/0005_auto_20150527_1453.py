# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0004_auto_20150527_1441'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='library',
            field=models.CharField(default='Leb', max_length=3, choices=[(b'Leb', b'Lebanon'), (b'KPL', b'Kilton')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='payment_type',
            field=models.CharField(default=b'cash', max_length=5, choices=[(b'cash', b'Cash'), (b'check', b'Check')]),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
