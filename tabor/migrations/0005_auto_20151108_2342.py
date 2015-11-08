# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabor', '0004_campgroup'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campgroup',
            options={'verbose_name': 'T\xe1bori csoport', 'verbose_name_plural': 'T\xe1bori csoportok'},
        ),
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name': 'Szem\xe9ly', 'verbose_name_plural': 'Szem\xe9lyek'},
        ),
    ]
