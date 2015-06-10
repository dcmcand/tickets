# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0019_tickets_sold'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locations',
            options={'verbose_name_plural': 'Locations'},
        ),
        migrations.AlterModelOptions(
            name='paymenttypes',
            options={'verbose_name_plural': 'Payment Types'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name_plural': 'Tickets'},
        ),
        migrations.AlterModelOptions(
            name='tickets_transactions',
            options={'verbose_name_plural': 'Tickets and Transactions'},
        ),
        migrations.AlterModelOptions(
            name='transactions',
            options={'verbose_name_plural': 'Transactions'},
        ),
    ]
