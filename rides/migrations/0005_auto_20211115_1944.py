# Generated by Django 3.2.9 on 2021-11-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0004_alter_ride_speed_mph'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='location',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='ride',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='ride',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
