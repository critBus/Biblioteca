# Generated by Django 4.2.7 on 2024-09-11 20:47

import apps.biblioteca.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("biblioteca", "0006_alter_materialaudiovisual_numero_serie_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="prestamo",
            options={"verbose_name": "Prestamo", "verbose_name_plural": "Prestamos"},
        ),
        migrations.AddField(
            model_name="revista",
            name="numero1",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Número"
            ),
        ),
        migrations.AlterField(
            model_name="asistencia",
            name="fecha",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro], verbose_name="Fecha"
            ),
        ),
        migrations.AlterField(
            model_name="inventario",
            name="fecha",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro], verbose_name="Fecha"
            ),
        ),
        migrations.AlterField(
            model_name="lecturade_libro",
            name="fecha",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro], verbose_name="Fecha"
            ),
        ),
        migrations.AlterField(
            model_name="libro",
            name="edicion",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator("^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
                ],
                verbose_name="Edición",
            ),
        ),
        migrations.AlterField(
            model_name="libro",
            name="fecha_adquisicion",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Adquisición",
            ),
        ),
        migrations.AlterField(
            model_name="libro",
            name="fecha_publicacion",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Publicación",
            ),
        ),
        migrations.AlterField(
            model_name="libro",
            name="genero",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Ficcion", "Ficcion"),
                    ("No ficción", "No ficción"),
                    ("Ciencia ficción", "Ciencia ficción"),
                    ("Fantasía", "Fantasía"),
                    ("Aventura", "Aventura"),
                    ("Policíaca", "Policíaca"),
                    ("Romántico", "Romántico"),
                ],
                max_length=256,
                null=True,
                verbose_name="Género",
            ),
        ),
        migrations.AlterField(
            model_name="librosdelmes",
            name="fecha",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro], verbose_name="Fecha"
            ),
        ),
        migrations.AlterField(
            model_name="materialaudiovisual",
            name="fecha_adquisicion",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Adquisición",
            ),
        ),
        migrations.AlterField(
            model_name="materialaudiovisual",
            name="fecha_produccion",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Producción",
            ),
        ),
        migrations.AlterField(
            model_name="materialaudiovisual",
            name="formato",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator("^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
                ],
                verbose_name="Formato",
            ),
        ),
        migrations.AlterField(
            model_name="materialaudiovisual",
            name="genero",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Ficcion", "Ficcion"),
                    ("No ficción", "No ficción"),
                    ("Ciencia ficción", "Ciencia ficción"),
                    ("Fantasía", "Fantasía"),
                    ("Aventura", "Aventura"),
                    ("Policíaca", "Policíaca"),
                    ("Romántico", "Romántico"),
                ],
                max_length=256,
                null=True,
                verbose_name="Género o Categoria",
            ),
        ),
        migrations.AlterField(
            model_name="muestrasmes",
            name="edad_maxima",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Edad Máxima Recomendada",
            ),
        ),
        migrations.AlterField(
            model_name="muestrasmes",
            name="edad_minima",
            field=models.IntegerField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(1)],
                verbose_name="Edad Minima Recomendada",
            ),
        ),
        migrations.AlterField(
            model_name="muestrasmes",
            name="genero",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator("^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
                ],
                verbose_name="Género o Categoria",
            ),
        ),
        migrations.AlterField(
            model_name="prestamo",
            name="fecha_prestamo",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Prestamo",
            ),
        ),
        migrations.AlterField(
            model_name="revista",
            name="fecha_adquisicion",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Adquisición",
            ),
        ),
        migrations.AlterField(
            model_name="revista",
            name="fecha_publicacion",
            field=models.DateField(
                validators=[apps.biblioteca.models.no_futuro],
                verbose_name="Fecha de Publicación",
            ),
        ),
        migrations.AlterField(
            model_name="revista",
            name="numero",
            field=models.CharField(
                blank=True, max_length=256, null=True, verbose_name="Número de Volumen"
            ),
        ),
        migrations.AlterField(
            model_name="suscriptor",
            name="centro_trabajo",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                verbose_name="Centro de Trbajo o Estudio ",
            ),
        ),
        migrations.AlterField(
            model_name="suscriptor",
            name="edad",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(120),
                ],
                verbose_name="Edad",
            ),
        ),
        migrations.AlterField(
            model_name="suscriptor",
            name="ocupacion",
            field=models.CharField(
                blank=True,
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator("^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$")
                ],
                verbose_name="Ocupación",
            ),
        ),
        migrations.AlterField(
            model_name="trabajador",
            name="edad",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(17),
                    django.core.validators.MaxValueValidator(100),
                ],
                verbose_name="Edad",
            ),
        ),
        migrations.AlterField(
            model_name="trabajador",
            name="expediente",
            field=models.IntegerField(
                validators=[
                    apps.biblioteca.models.length_validation_11,
                    django.core.validators.RegexValidator("^[0-9]{11}$"),
                    apps.biblioteca.models.not_empty_validation,
                ],
                verbose_name="Expediente",
            ),
        ),
    ]
