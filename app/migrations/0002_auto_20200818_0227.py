# Generated by Django 3.0.8 on 2020-08-18 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='home_number',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]