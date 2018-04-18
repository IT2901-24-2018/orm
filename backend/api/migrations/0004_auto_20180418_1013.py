# Generated by Django 2.0.2 on 2018-04-18 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_merge_20180411_0944'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadsegment',
            name='connlink',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='endnode',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='endposition',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='from_meter',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='hp',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='medium',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='number',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='roadsection',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='shortform',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='startnode',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='startposition',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='themecode',
        ),
        migrations.RemoveField(
            model_name='roadsegment',
            name='to_meter',
        ),
        migrations.AlterField(
            model_name='productiondata',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='startdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='roadsegment',
            name='stretchdistance',
            field=models.IntegerField(),
        ),
    ]