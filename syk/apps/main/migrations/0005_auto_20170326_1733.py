# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-26 17:33
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160713_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapEdge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vertexes', models.CharField(max_length=200)),
                ('hits', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MapVertex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('hits', models.PositiveIntegerField()),
                ('connections', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
            ],
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, help_text='Describe the main idea of your goal. Just for yourself.'),
        ),
    ]