# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='Name')),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, name=b'uuid', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
