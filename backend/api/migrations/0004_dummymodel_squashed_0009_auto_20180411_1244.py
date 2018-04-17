# Generated by Django 2.0.2 on 2018-04-13 08:47

import django.contrib.gis.db.models.fields
import django.contrib.postgres.operations
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('api', '0004_dummymodel'), ('api', '0005_auto_20180409_1248'), ('api', '0006_auto_20180409_1309'), ('api', '0007_postgis'), ('api', '0008_productiondata_segment'), ('api', '0009_auto_20180411_1244')]

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
                ('the_geom', django.contrib.gis.db.models.fields.LineStringField(srid=4326)),
            ],
            options={
                'abstract': False,
            },
        ),
        django.contrib.postgres.operations.CreateExtension(
            name='postgis',
        ),
        migrations.AddField(
            model_name='productiondata',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.DummyModel'),
        ),
    ]