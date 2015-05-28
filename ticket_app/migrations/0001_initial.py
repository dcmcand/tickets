# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_entered', models.DateField(auto_now_add=True)),
                ('sold', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ticket_numbers', models.PositiveIntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('check_number', models.PositiveIntegerField(null=True)),
                ('reported', models.BooleanField()),
                ('staff_initials', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='tickets',
            name='ticket_number',
            field=models.ForeignKey(to='ticket_app.Transactions'),
        ),
    ]
