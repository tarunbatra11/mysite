# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20151211_0857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='requests_received',
        ),
    ]
