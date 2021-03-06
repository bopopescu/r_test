# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-05 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('key', models.CharField(blank=True, max_length=250)),
                ('dataval', models.TextField(blank=True)),
                ('val', models.CharField(blank=True, max_length=20)),
                ('decision', models.CharField(blank=True, max_length=45)),
                ('ts', models.CharField(blank=True, max_length=45)),
                ('date', models.CharField(blank=True, max_length=250)),
                ('sc', models.CharField(blank=True, max_length=250)),
                ('dest', models.CharField(blank=True, max_length=45)),
                ('depart', models.CharField(blank=True, max_length=45)),
                ('arrival', models.CharField(blank=True, max_length=45)),
                ('airline', models.CharField(blank=True, max_length=45)),
                ('price', models.CharField(blank=True, max_length=45)),
                ('price_int', models.CharField(blank=True, max_length=45)),
                ('win_decision', models.CharField(blank=True, max_length=45)),
                ('win_value', models.CharField(blank=True, max_length=45)),
                ('current_winner', models.CharField(blank=True, max_length=100)),
                ('comp', models.CharField(blank=True, max_length=5000)),
                ('ts_recent', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'flightscrapdata',
            },
        ),
    ]
