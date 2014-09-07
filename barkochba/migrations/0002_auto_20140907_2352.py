# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkochba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='people',
            field=models.ManyToManyField(to=b'barkochba.Person', blank=True),
        ),
    ]
