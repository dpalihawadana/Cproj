# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Hermtweets', '0011_auto_20170410_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hermtweets',
            name='tweet_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 10, 11, 45, 2, 841226, tzinfo=utc)),
        ),
    ]
