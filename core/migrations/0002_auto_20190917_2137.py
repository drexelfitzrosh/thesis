# Generated by Django 2.0.1 on 2019-09-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='time',
            field=models.TimeField(),
        ),
    ]
