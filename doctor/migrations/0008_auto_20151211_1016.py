# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_remove_doctor_requests_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_message',
            field=models.CharField(blank=True, null=True, max_length=500),
        ),
    ]
