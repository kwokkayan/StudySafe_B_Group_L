# Generated by Django 4.0.3 on 2022-04-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudySafe_Core', '0005_alter_travelrecord_time_of_exit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelrecord',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visited', to='StudySafe_Core.hkumember'),
        ),
    ]
