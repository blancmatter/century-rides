# Generated by Django 3.2.9 on 2021-11-16 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0007_ride_cafe_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='distance',
            field=models.IntegerField(default=60),
            preserve_default=False,
        ),
    ]
