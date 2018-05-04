# Generated by Django 2.0.2 on 2018-05-04 13:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20180502_1016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherdata',
            name='time',
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='end_time_period',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 13, 59, 24, 436576, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weatherdata',
            name='start_time_period',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 4, 13, 59, 29, 700533, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='municipality',
            field=models.IntegerField(help_text='County and municipality number for that municipality.Example: 5001 for Trondheim'),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='county_and_municipality_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='degrees',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='segment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.RoadSegment'),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='unit',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='value',
            field=models.IntegerField(),
        ),
    ]
