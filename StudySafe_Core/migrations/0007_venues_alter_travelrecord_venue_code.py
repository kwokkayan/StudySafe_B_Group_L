# Generated by Django 4.0.3 on 2022-04-14 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('StudySafe_Core', '0006_alter_travelrecord_uid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('Venue_Code', models.CharField(db_column='Venue Code', max_length=20, primary_key=True, serialize=False)),
                ('Location', models.CharField(max_length=150)),
                ('Type', models.CharField(choices=[('LT', 'LT'), ('CR', 'CR'), ('TR', 'TR')], max_length=2)),
                ('Capacity', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='travelrecord',
            name='venue_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='StudySafe_Core.venues'),
        ),
    ]
