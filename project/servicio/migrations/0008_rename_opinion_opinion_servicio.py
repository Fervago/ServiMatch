# Generated by Django 3.2.25 on 2024-05-31 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0007_alter_opinion_opinion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='opinion',
            old_name='opinion',
            new_name='servicio',
        ),
    ]
