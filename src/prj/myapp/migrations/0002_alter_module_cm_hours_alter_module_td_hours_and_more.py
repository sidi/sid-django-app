# Generated by Django 5.1.4 on 2025-01-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='cm_hours',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='module',
            name='td_hours',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='module',
            name='tp_hours',
            field=models.FloatField(),
        ),
    ]
