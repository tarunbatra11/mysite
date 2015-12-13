# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0005_appointment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='appointment_message',
        ),
        migrations.RemoveField(
            model_name='account',
            name='appointment_status',
        ),
        migrations.RemoveField(
            model_name='account',
            name='feedback',
        ),
    ]
