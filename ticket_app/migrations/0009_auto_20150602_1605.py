# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0008_auto_20150602_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='total',
            field=models.IntegerField(),
        ),
    ]
