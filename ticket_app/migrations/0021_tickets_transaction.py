# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0020_auto_20150610_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='transaction',
            field=models.ForeignKey(related_name='ticket_number', on_delete=django.db.models.deletion.SET_NULL, to='ticket_app.Transactions', null=True),
        ),
    ]
