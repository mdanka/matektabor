# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='camp_group',
            field=models.CharField(default=b'', max_length=200, verbose_name='T\xe1bori csoport', blank=True),
            preserve_default=True,
        ),
    ]
