# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0007_auto_20150530_1149'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets_Transactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket', models.ForeignKey(to='ticket_app.Tickets')),
            ],
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='ticket_number',
        ),
        migrations.AddField(
            model_name='transactions',
            name='total',
            field=models.FloatField(default=10.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tickets_transactions',
            name='transactions',
            field=models.ForeignKey(to='ticket_app.Transactions'),
        ),
    ]
