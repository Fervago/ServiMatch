# Generated by Django 3.2.25 on 2024-05-31 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('servicio', '0006_opinion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='opinion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='servicio.ofrecerservicio'),
        ),
    ]
