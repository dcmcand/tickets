# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0018_remove_tickets_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='sold',
            field=models.BooleanField(default=False),
        ),
    ]
