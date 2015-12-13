# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0004_doctor_requests_received'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('appointment_message', models.CharField(max_length=500, null=True)),
                ('request_date', models.DateTimeField(blank=True, null=True)),
                ('doctor', models.OneToOneField(to='doctor.Doctor')),
                ('patient', models.OneToOneField(to='doctor.Account')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
