# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0016_transactions_date_reported'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactions',
            name='total',
        ),
    ]
