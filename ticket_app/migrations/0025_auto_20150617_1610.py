# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0024_tickets_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('location', models.ForeignKey(to='ticket_app.Locations')),
            ],
        ),
        migrations.AlterModelOptions(
            name='transactions',
            options={'ordering': ['date'], 'verbose_name_plural': 'Transactions'},
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='date_reported',
        ),
        migrations.AddField(
            model_name='transactions',
            name='report',
            field=models.ForeignKey(blank=True, to='ticket_app.Report', null=True),
        ),
    ]
