# Generated by Django 3.2.9 on 2021-11-15 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0002_ride_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='date',
            field=models.DateField(blank=True),
        ),
    ]
