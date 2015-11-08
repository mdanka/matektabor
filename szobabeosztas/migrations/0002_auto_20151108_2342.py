# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('szobabeosztas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='camp',
            options={'verbose_name': 'T\xe1bor', 'verbose_name_plural': 'T\xe1borok'},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'verbose_name': 'Szoba', 'verbose_name_plural': 'Szob\xe1k'},
        ),
        migrations.AlterField(
            model_name='camp',
            name='group',
            field=models.ForeignKey(verbose_name='Csoport', to='tabor.CampGroup'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='camp',
            field=models.ForeignKey(verbose_name='T\xe1bor', to='szobabeosztas.Camp'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='people',
            field=models.ManyToManyField(to='tabor.Person', verbose_name='Lak\xf3k', blank=True),
            preserve_default=True,
        ),
    ]
