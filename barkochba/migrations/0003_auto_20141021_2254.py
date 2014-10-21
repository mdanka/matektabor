# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkochba', '0002_auto_20141021_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='solution',
            field=models.TextField(default='?', verbose_name='Megold\xe1s'),
        ),
        migrations.AlterField(
            model_name='story',
            name='story',
            field=models.TextField(default='?', verbose_name='T\xf6rt\xe9net'),
        ),
    ]
