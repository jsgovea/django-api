# Generated by Django 5.0.6 on 2024-07-04 03:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_climates_planet_climate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planet',
            old_name='terrains',
            new_name='terrain',
        ),
    ]
