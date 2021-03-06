# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-21 03:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polling', '0008_auto_20160919_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitalsubjectregistration',
            name='subject_detail',
        ),
        migrations.RemoveField(
            model_name='hospitalsubjectregistration',
            name='subject_insurance_policy_detail',
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='DoctorID',
            field=models.CharField(default=datetime.datetime(2016, 9, 21, 3, 44, 49, 18000, tzinfo=utc), max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='FullAddress',
            field=models.TextField(default=datetime.datetime(2016, 9, 21, 3, 44, 57, 426000, tzinfo=utc), max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='FullName',
            field=models.CharField(default='Test', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='InsurancePlan',
            field=models.CharField(default='Wellness', max_length=300),
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='InsurancePolicyID',
            field=models.CharField(default=b'C496F8B28', max_length=400),
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='Patient_ID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitalsubjectregistration',
            name='RegisterPatientRemoteMonitoring',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospitalsubjectregistration',
            name='Patient_History',
            field=models.TextField(default=datetime.datetime(2016, 9, 21, 3, 45, 40, 244000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
