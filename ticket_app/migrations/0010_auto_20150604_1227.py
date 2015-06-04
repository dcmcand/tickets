# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0009_auto_20150602_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='location',
            field=models.ForeignKey(to='ticket_app.Locations'),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='location',
            field=models.ForeignKey(to='ticket_app.Locations'),
        ),
    ]
