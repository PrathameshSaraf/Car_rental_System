# Generated by Django 4.1rc1 on 2022-08-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_title',
            field=models.CharField(max_length=2000),
        ),
    ]
