# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0016_auto_20151212_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='approved_status',
            field=models.CharField(default='pending', max_length=8),
        ),
    ]
