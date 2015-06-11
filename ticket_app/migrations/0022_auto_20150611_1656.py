# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0021_tickets_transaction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='transaction',
            field=models.ForeignKey(related_name='ticket_number', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='ticket_app.Transactions', null=True),
        ),
    ]
