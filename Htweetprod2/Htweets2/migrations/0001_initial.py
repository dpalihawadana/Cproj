# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Htweets2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet_id', models.BigIntegerField(blank=True)),
                ('tweet_timestamp', models.CharField(blank=True, max_length=200)),
                ('tweet_screenname', models.CharField(blank=True, max_length=200)),
                ('tweet_favour_count', models.CharField(blank=True, max_length=200)),
                ('tweet_recount', models.BigIntegerField(blank=True)),
                ('tweet_location', models.CharField(blank=True, max_length=200, null=True)),
                ('tweet_text', models.TextField(blank=True)),
                ('tweet_media_entities', models.URLField(blank=True)),
            ],
        ),
    ]
