# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0012_tickets_date_sold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='date_sold',
            field=models.DateField(null=True, blank=True),
        ),
    ]
