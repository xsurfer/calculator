# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='expression',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
