# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-08-15 12:58
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0004_auto_20170501_0637'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestproblem',
            name='statistic_info',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AddField(
            model_name='problem',
            name='statistic_info',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]