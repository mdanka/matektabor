# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='N\xe9v')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='C\xedm')),
                ('story', models.TextField(verbose_name='T\xf6rt\xe9net')),
                ('solution', models.TextField(verbose_name='Megold\xe1s')),
                ('people', models.ManyToManyField(to='barkochba.Person')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
