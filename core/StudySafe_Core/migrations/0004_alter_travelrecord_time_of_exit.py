# Generated by Django 4.0.3 on 2022-04-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudySafe_Core', '0003_travelrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelrecord',
            name='time_of_exit',
            field=models.DateTimeField(default=None),
        ),
    ]