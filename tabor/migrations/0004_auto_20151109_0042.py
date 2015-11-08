# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabor', '0003_auto_20141021_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='Csoport neve')),
            ],
            options={
                'verbose_name': 'T\xe1bori csoport',
                'verbose_name_plural': 'T\xe1bori csoportok',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Szem\xe9ly', 'verbose_name_plural': 'Szem\xe9lyek'},
        ),
    ]
