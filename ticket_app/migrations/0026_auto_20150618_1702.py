# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0025_auto_20150617_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Transactions'},
        ),
    ]
