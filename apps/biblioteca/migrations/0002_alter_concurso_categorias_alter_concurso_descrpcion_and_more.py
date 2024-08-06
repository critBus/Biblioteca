# Generated by Django 4.2.7 on 2024-08-02 21:10

import apps.biblioteca.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concurso',
            name='categorias',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='descrpcion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='modalidad',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ,]+$')], verbose_name='Modalidad'),
        ),
        migrations.AlterField(
            model_name='concurso',
            name='nombre',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='autor',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='descripcion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='edicion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Edición'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Editorial'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(choices=[('Ficcion', 'Ficcion'), ('No ficción', 'No ficción'), ('Ciencia ficción', 'Ciencia ficción'), ('Fantasía', 'Fantasía'), ('Aventura', 'Aventura'), ('Policíaca', 'Policíaca'), ('Romántico', 'Romántico')], max_length=256, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='numero_copias',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='numero_serie',
            field=models.IntegerField(max_length=256, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='ubicacion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='creador',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Creador o Autor'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='descripcion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='formato',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Formato'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='genero',
            field=models.CharField(choices=[('Ficcion', 'Ficcion'), ('No ficción', 'No ficción'), ('Ciencia ficción', 'Ciencia ficción'), ('Fantasía', 'Fantasía'), ('Aventura', 'Aventura'), ('Policíaca', 'Policíaca'), ('Romántico', 'Romántico')], max_length=256, verbose_name='Género o Categoria'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='numero_copias',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='numero_serie',
            field=models.CharField(max_length=256, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='productora',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Productora'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='titulo',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='materialaudiovisual',
            name='ubicacion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='cantidad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='costo_adqisicion',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Costo de Adquisición'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='dimenciones',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dimenciones'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='nombre_tipoMueble',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre del Mueble'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='numero_serie',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie'),
        ),
        migrations.AlterField(
            model_name='mobiliario',
            name='ubicacion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='autor',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='descrpcion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='direccion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='edad_maxima',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Máxima Recomendada'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='edad_minima',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Minima Recomendada'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='genero',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Género o Categoria'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='nombre_muestra',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='responsable',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Responsable'),
        ),
        migrations.AlterField(
            model_name='muestrasmes',
            name='tipo_muestra',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Tipo de Muestra'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='descripcion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='editorial',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Editorial'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='nombre',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre de la Revista'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='numero',
            field=models.CharField(max_length=256, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Volumen'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='numero_copias',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='numero_serie',
            field=models.CharField(max_length=256, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='perioricidad',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Perioricidad'),
        ),
        migrations.AlterField(
            model_name='revista',
            name='ubicacion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='Telefono',
            field=models.CharField(max_length=8, unique=True, validators=[apps.biblioteca.models.length_validation_8, django.core.validators.RegexValidator('^[0-9]{8}$'), apps.biblioteca.models.not_empty_validation], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='ci',
            field=models.IntegerField(validators=[apps.biblioteca.models.length_validation_11, django.core.validators.RegexValidator('^[0-9]{11}$'), apps.biblioteca.models.not_empty_validation], verbose_name='CI'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='direccion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='nivel_escolar',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nivel de Escolaridad'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='nombre',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='ocupacion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ocupación'),
        ),
        migrations.AlterField(
            model_name='suscriptor',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=256, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='Telefono',
            field=models.CharField(max_length=256, validators=[apps.biblioteca.models.length_validation_8, django.core.validators.RegexValidator('^[0-9]{8}$'), apps.biblioteca.models.not_empty_validation], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='ci',
            field=models.IntegerField(validators=[apps.biblioteca.models.length_validation_11, django.core.validators.RegexValidator('^[0-9]{11}$'), apps.biblioteca.models.not_empty_validation], verbose_name='CI'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='direccion',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='expediente',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Expediente'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nivel_escolar',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nivel de Escolaridad'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='nombre',
            field=models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='sexo',
            field=models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=256, verbose_name='Sexo'),
        ),
    ]