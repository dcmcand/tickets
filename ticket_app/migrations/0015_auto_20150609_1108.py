# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0014_auto_20150609_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets_transactions',
            name='ticket',
            field=models.OneToOneField(to='ticket_app.Tickets'),
        ),
    ]
