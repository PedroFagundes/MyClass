# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0001_initial'),
        ('areas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('nome', models.CharField(max_length=45)),
                ('area', models.ForeignKey(to='areas.Areas')),
                ('campus', models.ForeignKey(to='campus.Campus')),
            ],
        ),
    ]
