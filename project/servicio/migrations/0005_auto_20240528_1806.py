# Generated by Django 3.2.25 on 2024-05-28 21:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicio', '0004_auto_20240528_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contratarservicio',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='ofrecerservicio',
            name='usuario',
        ),
        migrations.AddField(
            model_name='servicio',
            name='usuario',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
