# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0011_auto_20150604_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='date_sold',
            field=models.DateField(default=datetime.datetime(2015, 6, 4, 20, 51, 18, 808562, tzinfo=utc), blank=True),
            preserve_default=False,
        ),
    ]
