# Generated by Django 2.0.2 on 2018-04-06 11:16

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20180406_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='DummyModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('the_geom', django.contrib.gis.db.models.fields.LineStringField(srid=32633)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
