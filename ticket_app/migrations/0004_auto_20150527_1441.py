# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0003_auto_20150527_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='ticket_numbers',
        ),
        migrations.AddField(
            model_name='transactions',
            name='ticket_number',
            field=models.ForeignKey(to='ticket_app.Tickets', default=12345, to_field=b'ticket_number'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tickets',
            name='ticket_number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
