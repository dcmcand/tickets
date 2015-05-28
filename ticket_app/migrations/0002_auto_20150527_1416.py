# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='ticket_number',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='ticket_numbers',
            field=models.ForeignKey(to='ticket_app.Transactions'),
        ),
    ]
