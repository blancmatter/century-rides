# Generated by Django 3.2.9 on 2021-11-15 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0003_alter_ride_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='speed_mph',
            field=models.IntegerField(default=15),
        ),
    ]
