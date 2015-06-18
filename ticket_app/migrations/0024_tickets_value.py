# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0023_remove_tickets_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='value',
            field=models.PositiveIntegerField(default=10),
        ),
    ]
