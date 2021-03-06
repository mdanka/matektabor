# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order_number', models.PositiveIntegerField(default=0, verbose_name='Sorsz\xe1m')),
                ('title', models.CharField(max_length=200, verbose_name='C\xedm')),
                ('story', models.TextField(verbose_name='T\xf6rt\xe9net')),
                ('solution', models.TextField(verbose_name='Megold\xe1s')),
                ('people', models.ManyToManyField(to='tabor.Person', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
