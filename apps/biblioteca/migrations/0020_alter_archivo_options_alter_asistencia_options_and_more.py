# Generated by Django 4.2.7 on 2025-04-15 16:32

import apps.biblioteca.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0019_libro_cantidad_paginas_libro_materia_libro_pais_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='archivo',
            options={'verbose_name': 'Archivo Histórioco', 'verbose_name_plural': 'Archivos Históricos'},
        ),
        migrations.AlterModelOptions(
            name='asistencia',
            options={'verbose_name': 'Informe de Asitecias', 'verbose_name_plural': 'Informes de Asistencias'},
        ),
        migrations.AlterModelOptions(
            name='mobiliario',
            options={'verbose_name': 'Mobiliario', 'verbose_name_plural': 'Mobiliarios'},
        ),
        migrations.AlterModelOptions(
            name='prestamo',
            options={'verbose_name': 'Préstamo', 'verbose_name_plural': 'Préstamos'},
        ),
        migrations.AlterModelOptions(
            name='revista',
            options={'verbose_name': 'Revista', 'verbose_name_plural': 'Revistas'},
        ),
        migrations.AlterField(
            model_name='concurso',
            name='categorias',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='cantidad_prestamo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Préstamos'),
        ),
        migrations.AlterField(
            model_name='libroinfantil',
            name='cantidad_prestamo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Préstamos'),
        ),
        migrations.AlterField(
            model_name='libroinfantil',
            name='edad_minima',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Mínima Recomendada'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='cantidad_prestamo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de préstamos'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='genero',
            field=models.CharField(blank=True, choices=[('Ficción', 'Ficción'), ('No ficción', 'No ficción'), ('Ciencia ficción', 'Ciencia ficción'), ('Fantasía', 'Fantasía'), ('Aventura', 'Aventura'), ('Policíaca', 'Policíaca'), ('Romántico', 'Romántico')], max_length=256, null=True, verbose_name='Género o Categoría'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='dimenciones',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dimensiones'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='edad_minima',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Mínima Recomendada'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='genero',
            field=models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Género o Categoría'),
        ),
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_prestamo',
            field=models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Préstamo'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='cantidad_prestamo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de préstamos'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='nombre',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre de la Revista'),
        ),
    ]
