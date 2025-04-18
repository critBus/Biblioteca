# Generated by Django 4.2.7 on 2025-04-16 17:16

import apps.biblioteca.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Concurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fecha_cierre', models.DateField(verbose_name='Fecha de Cierre')),
                ('nombre', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre')),
                ('descrpcion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción')),
                ('categorias', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Categoría')),
                ('modalidad', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ,]+$')], verbose_name='Modalidad')),
            ],
            options={
                'verbose_name': 'Concurso',
                'verbose_name_plural': 'Concursos',
            },
        ),
        migrations.CreateModel(
            name='ConfiguracionBiblio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_maximo', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'Configuraciones de la Biblioteca',
                'verbose_name_plural': 'Configuraciones de la Biblioteca ',
            },
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor_estancia', models.FloatField(default=0)),
                ('peso', models.FloatField(default=0)),
                ('titulo', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título')),
                ('editorial', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Editorial')),
                ('autor', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Autor')),
                ('fecha_publicacion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Publicación')),
                ('edicion', models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Edición')),
                ('estado', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=256, verbose_name='Estado')),
                ('ubicacion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación')),
                ('descripcion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción')),
                ('genero', models.CharField(blank=True, choices=[('Ficcion', 'Ficcion'), ('No ficción', 'No ficción'), ('Ciencia ficción', 'Ciencia ficción'), ('Fantasía', 'Fantasía'), ('Aventura', 'Aventura'), ('Policíaca', 'Policíaca'), ('Romántico', 'Romántico')], max_length=256, null=True, verbose_name='Género')),
                ('fecha_adquisicion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Adquisición')),
                ('numero_copias', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles')),
                ('numero_serie', models.IntegerField(max_length=256, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie')),
                ('materia', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Materia')),
                ('pais', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='País')),
                ('resumen', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Resumen del Contenido')),
                ('cantidad_prestamo', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Préstamos')),
                ('cantidad_paginas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Páginas')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
            },
        ),
        migrations.CreateModel(
            name='LibroInfantil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor_estancia', models.FloatField(default=0)),
                ('peso', models.FloatField(default=0)),
                ('titulo', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título')),
                ('editorial', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Editorial')),
                ('autor', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Autor')),
                ('fecha_publicacion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Publicación')),
                ('edicion', models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Edición')),
                ('estado', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=256, verbose_name='Estado')),
                ('ubicacion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación')),
                ('descripcion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción')),
                ('genero', models.CharField(blank=True, choices=[('Ficcion', 'Ficcion'), ('No ficción', 'No ficción'), ('Ciencia ficción', 'Ciencia ficción'), ('Fantasía', 'Fantasía'), ('Aventura', 'Aventura'), ('Policíaca', 'Policíaca'), ('Romántico', 'Romántico')], max_length=256, null=True, verbose_name='Género')),
                ('fecha_adquisicion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Adquisición')),
                ('numero_copias', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles')),
                ('numero_serie', models.IntegerField(max_length=256, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie')),
                ('materia', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Materia')),
                ('pais', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='País')),
                ('resumen', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Resumen del Contenido')),
                ('cantidad_prestamo', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Préstamos')),
                ('cantidad_paginas', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de Páginas')),
                ('ilustracioes', models.BooleanField(default=False)),
                ('edad_minima', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Mínima Recomendada')),
                ('edad_maxima', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Máxima Recomendada')),
            ],
            options={
                'verbose_name': 'Libro Infantil',
                'verbose_name_plural': 'LIbros Infantiles',
            },
        ),
        migrations.CreateModel(
            name='MaterialAudiovisual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título')),
                ('creador', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Creador o Autor')),
                ('fecha_produccion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Producción')),
                ('productora', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Productora')),
                ('estado', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=256, verbose_name='Estado')),
                ('ubicacion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación')),
                ('descripcion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción')),
                ('genero', models.CharField(blank=True, choices=[('Ficción', 'Ficción'), ('No ficción', 'No ficción'), ('Ciencia ficción', 'Ciencia ficción'), ('Fantasía', 'Fantasía'), ('Aventura', 'Aventura'), ('Policíaca', 'Policíaca'), ('Romántico', 'Romántico')], max_length=256, null=True, verbose_name='Género o Categoría')),
                ('formato', models.CharField(blank=True, choices=[('MP4', 'MP4'), ('AVI', 'AVI'), ('MOV', 'MOV'), ('WMV', 'WMV'), ('FLV', 'FLV'), ('WebM', 'WebM'), ('MPEG', 'MPEG'), ('3GP', '3GP'), ('AVCHD', 'AVCHD')], max_length=256, null=True, verbose_name='Formato')),
                ('fecha_adquisicion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Adquisición')),
                ('numero_copias', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles')),
                ('numero_serie', models.CharField(max_length=256, verbose_name='Número de Serie')),
                ('cantidad_prestamo', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de préstamos')),
            ],
            options={
                'verbose_name': 'Material Audivisual',
                'verbose_name_plural': 'Materiales Audiovisuales',
            },
        ),
        migrations.CreateModel(
            name='Mobiliario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_tipoMueble', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre del Mueble')),
                ('numero_serie', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Serie')),
                ('ubicacion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación')),
                ('dimenciones', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dimensiones')),
                ('costo_adqisicion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Costo de Adquisición')),
                ('cantidad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad')),
                ('estado', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=256, verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Mobiliario',
                'verbose_name_plural': 'Mobiliarios',
            },
        ),
        migrations.CreateModel(
            name='MuestrasMes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_muestra', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Título')),
                ('tipo_muestra', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Tipo de Muestra')),
                ('autor', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Autor')),
                ('responsable', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Responsable')),
                ('descrpcion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción')),
                ('genero', models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Género o Categoría')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de Inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de Fin')),
                ('horario_inicio', models.TimeField(verbose_name='Horario de inicio')),
                ('horario_Cierre', models.TimeField(verbose_name='Horario de cierre')),
                ('edad_minima', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Mínima Recomendada')),
                ('edad_maxima', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Edad Máxima Recomendada')),
                ('direccion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Dirección')),
            ],
            options={
                'verbose_name': 'Muestra del Mes',
                'verbose_name_plural': 'Muestras del Mes',
            },
        ),
        migrations.CreateModel(
            name='Revista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factor_estancia', models.FloatField(default=0)),
                ('peso', models.FloatField(default=0)),
                ('nombre', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre de la Revista')),
                ('perioricidad', models.CharField(choices=[('Semanal', 'Semanal'), ('Quincenal', 'Quincenal'), ('Mensual', 'Mensual'), ('Bimestral', 'Bimestral'), ('Trimestral', 'Trimestral'), ('Semestral', 'Semestral'), ('Anual', 'Anual'), ('Irregular', 'Irregular')], max_length=256, verbose_name='Perioricidad')),
                ('numero', models.CharField(blank=True, max_length=256, null=True, verbose_name='Número de Volumen')),
                ('numero1', models.CharField(blank=True, max_length=256, null=True, verbose_name='Número')),
                ('fecha_publicacion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Publicación')),
                ('editorial', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Editorial')),
                ('Pais', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='País')),
                ('estado', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=256, verbose_name='Estado')),
                ('ubicacion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ubicación')),
                ('descripcion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Descripción')),
                ('fecha_adquisicion', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Adquisición')),
                ('numero_copias', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Número de Copias Disponibles')),
                ('numero_serie', models.CharField(max_length=256, verbose_name='Número de Serie')),
                ('cantidad_prestamo', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de préstamos')),
            ],
            options={
                'verbose_name': 'Revista',
                'verbose_name_plural': 'Revistas',
            },
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre')),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(17), django.core.validators.MaxValueValidator(100)], verbose_name='Edad')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=256, verbose_name='Sexo')),
                ('Telefono', models.CharField(max_length=256, validators=[apps.biblioteca.models.length_validation_8, django.core.validators.RegexValidator('^[0-9]{8}$'), apps.biblioteca.models.not_empty_validation], verbose_name='Teléfono')),
                ('ci', models.IntegerField(validators=[apps.biblioteca.models.length_validation_11, django.core.validators.RegexValidator('^[0-9]{11}$'), apps.biblioteca.models.not_empty_validation], verbose_name='CI')),
                ('expediente', models.IntegerField(validators=[apps.biblioteca.models.length_validation_11, django.core.validators.RegexValidator('^[0-9]{11}$'), apps.biblioteca.models.not_empty_validation], verbose_name='Expediente')),
                ('direccion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ#/ ]+$')], verbose_name='Dirección')),
                ('sindicato', models.BooleanField(default=False)),
                ('nivel_escolar', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nivel de Escolaridad')),
            ],
            options={
                'verbose_name': 'Trabajador',
                'verbose_name_plural': 'Trabajadores',
            },
        ),
        migrations.CreateModel(
            name='UsuariosEventuales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(validators=[apps.biblioteca.models.no_pasado], verbose_name='Fecha de vencimiento')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario Eventual',
                'verbose_name_plural': 'Usuarios Eventuales',
            },
        ),
        migrations.CreateModel(
            name='Suscriptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nombre')),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(120)], verbose_name='Edad')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=256, verbose_name='Sexo')),
                ('Telefono', models.CharField(max_length=8, unique=True, validators=[apps.biblioteca.models.length_validation_8, django.core.validators.RegexValidator('^[0-9]{8}$'), apps.biblioteca.models.not_empty_validation], verbose_name='Teléfono')),
                ('ci', models.IntegerField(validators=[apps.biblioteca.models.length_validation_11, django.core.validators.RegexValidator('^[0-9]{11}$'), apps.biblioteca.models.not_empty_validation], verbose_name='CI')),
                ('centro_trabajo', models.CharField(blank=True, max_length=256, null=True, verbose_name='Centro de Trbajo o Estudio ')),
                ('ocupacion', models.CharField(blank=True, max_length=256, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Ocupación')),
                ('direccion', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ/# ]+$')], verbose_name='Dirección')),
                ('sindicato', models.BooleanField(default=False)),
                ('nivel_escolar', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$')], verbose_name='Nivel de Escolaridad')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha de Préstamo')),
                ('fecha_entrga', models.DateField(verbose_name='Fecha de Entrega')),
                ('devolucion', models.BooleanField(default=False)),
                ('libro', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
                ('libro_infantil', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libroinfantil')),
                ('revista', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='biblioteca.revista')),
                ('suscriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.suscriptor')),
            ],
            options={
                'verbose_name': 'Préstamo',
                'verbose_name_plural': 'Préstamos',
            },
        ),
        migrations.CreateModel(
            name='LibrosDelMes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
            ],
            options={
                'verbose_name': 'Libro del mes',
                'verbose_name_plural': 'Libros del Mes',
            },
        ),
        migrations.CreateModel(
            name='Lecturade_libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro')),
                ('suscriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.suscriptor')),
            ],
            options={
                'verbose_name': 'Lectura de libro',
                'verbose_name_plural': 'Lecturas de libros',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True, validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha')),
                ('libros', models.ManyToManyField(to='biblioteca.libro')),
                ('materiales_audiovisuales', models.ManyToManyField(to='biblioteca.materialaudiovisual')),
                ('mobiliarios', models.ManyToManyField(to='biblioteca.mobiliario')),
                ('revistas', models.ManyToManyField(to='biblioteca.revista')),
            ],
            options={
                'verbose_name': 'Inventario',
                'verbose_name_plural': 'Inventarios',
            },
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(validators=[apps.biblioteca.models.no_futuro], verbose_name='Fecha')),
                ('horas', models.IntegerField(verbose_name='Horas Trabajadas')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.trabajador')),
            ],
            options={
                'verbose_name': 'Informe de Asitecias',
                'verbose_name_plural': 'Informes de Asistencias',
            },
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField(verbose_name='Fecha de inicio')),
                ('fecha_fin', models.DateField(verbose_name='Fecha de fin')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Archivo Histórico',
                'verbose_name_plural': 'Archivos Históricos',
            },
        ),
    ]
