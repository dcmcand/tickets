# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0002_auto_20150527_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='ticket_numbers',
            field=models.ForeignKey(to='ticket_app.Tickets'),
        ),
    ]
