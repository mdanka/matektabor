# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabor', '0004_auto_20151109_0042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=200, verbose_name='Sorsz\xe1m')),
                ('group', models.ForeignKey(verbose_name='Csoport', to='tabor.CampGroup')),
            ],
            options={
                'verbose_name': 'T\xe1bor',
                'verbose_name_plural': 'T\xe1borok',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Szoban\xe9v')),
                ('camp', models.ForeignKey(verbose_name='T\xe1bor', to='szobabeosztas.Camp')),
                ('people', models.ManyToManyField(to='tabor.Person', verbose_name='Lak\xf3k', blank=True)),
            ],
            options={
                'verbose_name': 'Szoba',
                'verbose_name_plural': 'Szob\xe1k',
            },
            bases=(models.Model,),
        ),
    ]
