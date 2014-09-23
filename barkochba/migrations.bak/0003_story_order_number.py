# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkochba', '0002_auto_20140907_2352'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='order_number',
            field=models.PositiveIntegerField(default=0, verbose_name='Sorsz\xe1m'),
            preserve_default=True,
        ),
    ]
