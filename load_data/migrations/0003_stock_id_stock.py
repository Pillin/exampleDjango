# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('load_data', '0002_auto_20141218_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='id_stock',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
