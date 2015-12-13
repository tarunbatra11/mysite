# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_appointment_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='approved_status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
