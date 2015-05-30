# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_app', '0006_tickets_library'),
    ]

    operations = [
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(unique=True, max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='tickets',
            name='library',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='library',
        ),
        migrations.AlterField(
            model_name='transactions',
            name='payment_type',
            field=models.ForeignKey(to='ticket_app.PaymentTypes'),
        ),
        migrations.AddField(
            model_name='tickets',
            name='location',
            field=models.ForeignKey(to='ticket_app.Locations', default='Lebanon Library', to_field=b'name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transactions',
            name='location',
            field=models.ForeignKey(to='ticket_app.Locations', default='Lebanon Library', to_field=b'name'),
            preserve_default=False,
        ),
    ]
