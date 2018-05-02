# Generated by Django 2.0.2 on 2018-04-30 15:17

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.contrib.gis.geos.point


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_merge_20180418_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='productiondata',
            name='closest_point',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(10.356343049613752, 63.397435490163907), srid=4326),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='category',
            field=models.CharField(help_text='Road segment category. Example: K', max_length=4),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='county',
            field=models.IntegerField(help_text='County identifier.  Example: 50'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='href',
            field=models.CharField(help_text='Link to NVDB for this unique segment', max_length=150),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='municipality',
            field=models.IntegerField(help_text='Municipality number for that county.Example: 01 for Trondheim'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='region',
            field=models.IntegerField(help_text='Region number. Example: 4'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='roadsectionid',
            field=models.IntegerField(help_text='Unique identifier for the road segment. Example: 171712'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='startdate',
            field=models.DateField(help_text='Start date for the road segment. Example: 2018-04-20'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='status',
            field=models.CharField(help_text='Road status. Example: G', max_length=4),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='stretchdistance',
            field=models.IntegerField(help_text='Length of the road segment. Example 31'),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='the_geom',
            field=django.contrib.gis.db.models.fields.LineStringField(help_text='Linestring according to ISO 19162:2015. Example: SRID=4326;LINESTRING (10.37634290477487 63.3478716972899, 10.37656821856063 63.34786722088941)', srid=4326),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='typeofroad',
            field=models.CharField(help_text='A description of the road type. Example: gangOgSykkelvei', max_length=100),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='vrefshortform',
            field=models.CharField(help_text='A combination of multiple fields. Example: 5001 Kg97587 hp1 m349-380', max_length=255),
        ),
    ]