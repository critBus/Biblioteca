# Generated by Django 4.2.7 on 2024-08-28 18:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0003_asistencia_horas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suscriptor',
            name='direccion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ/# ]+$')], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='direccion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ#/ ]+$')], verbose_name='Dirección'),
        ),
    ]