# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_auto_20151209_0650'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='appointment_message',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='appointment_status',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='account',
            name='feedback',
            field=models.CharField(max_length=300, null=True),
            preserve_default=True,
        ),
    ]
