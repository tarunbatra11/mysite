# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0008_auto_20151211_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_message',
            field=models.CharField(max_length=500),
        ),
    ]
