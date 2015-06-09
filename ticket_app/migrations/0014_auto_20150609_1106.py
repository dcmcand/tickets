# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0013_auto_20150604_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets_transactions',
            name='ticket',
            field=models.ForeignKey(to='ticket_app.Tickets', unique=True),
        ),
    ]
