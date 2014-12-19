# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='cod_local',
            field=models.CharField(max_length=150),
            preserve_default=True,
        ),
    ]
