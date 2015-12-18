# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_auto_20151216_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('feedback_given', models.CharField(max_length=500)),
                ('feedback_time', models.DateTimeField(null=True, blank=True)),
                ('approved_status', models.CharField(max_length=8, default='pending')),
                ('doctor', models.ForeignKey(to='doctor.Doctor')),
                ('patient', models.ForeignKey(to='doctor.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
