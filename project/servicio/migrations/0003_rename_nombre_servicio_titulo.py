# Generated by Django 3.2.25 on 2024-05-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0002_auto_20240526_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='nombre',
            new_name='titulo',
        ),
    ]
