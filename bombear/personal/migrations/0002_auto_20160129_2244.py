# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bombero',
            name='numero_de_ioma',
            field=models.CharField(max_length='255', null=True, blank=True, verbose_name='Numero de IOMA'),
        ),
    ]
