# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('leader', models.IntegerField(default=0)),
                ('goodsense', models.IntegerField(default=0)),
                ('freeart', models.IntegerField(default=0)),
                ('trus', models.IntegerField(default=0)),
                ('session', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
