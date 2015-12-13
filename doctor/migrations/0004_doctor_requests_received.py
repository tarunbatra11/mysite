# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20151209_0701'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='requests_received',
            field=models.CharField(null=True, max_length=500),
            preserve_default=True,
        ),
    ]
