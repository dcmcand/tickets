# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0017_remove_transactions_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='sold',
        ),
    ]
