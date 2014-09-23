# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barkochba', '0003_story_order_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterField(
            model_name='story',
            name='people',
            field=models.ManyToManyField(to=b'tabor.Person', blank=True),
        ),
    ]
