# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabor', '0004_campgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200, verbose_name='Sorsz\xe1m')),
                ('group', models.ForeignKey(to='tabor.CampGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Szoban\xe9v')),
                ('camp', models.ForeignKey(to='szobabeosztas.Camp')),
                ('people', models.ManyToManyField(to='tabor.Person', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
