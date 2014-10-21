# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkochba', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name': 'Barkochbat\xf6rt\xe9net', 'verbose_name_plural': 'Barkochbat\xf6rt\xe9net'},
        ),
    ]
