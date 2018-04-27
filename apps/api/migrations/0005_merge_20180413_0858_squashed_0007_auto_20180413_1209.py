# Generated by Django 2.0.2 on 2018-04-18 11:09

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.linestring
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('api', '0005_merge_20180413_0858'), ('api', '0006_auto_20180413_0912'), ('api', '0007_auto_20180413_1209')]

    dependencies = [
        ('api', '0003_merge_20180411_0944'),
        ('api', '0004_dummymodel_squashed_0009_auto_20180411_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productiondata',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RoadSegment'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='stretchdistance',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='DummyModel',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='coordinates',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='srid',
        ),
        migrations.AddField(
            model_name='roadsegment',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.LineStringField(default=django.contrib.gis.geos.linestring.LineString((10.5361787687115, 63.4125731083948), (10.5361924532311, 63.4126037467593)), srid=4326),
            preserve_default=False,
        ),
    ]