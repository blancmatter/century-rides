# Generated by Django 3.2.9 on 2021-11-16 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0006_auto_20211116_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='ride',
            name='cafe_stop',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
