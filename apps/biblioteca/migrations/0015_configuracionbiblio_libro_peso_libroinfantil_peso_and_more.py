# Generated by Django 4.2.7 on 2024-12-15 21:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0014_libro_factor_estancia_libroinfantil_factor_estancia'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionBiblio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso_maximo', models.FloatField()),
            ],
            options={
                'verbose_name': 'Configuraciones de la Biblioteca',
                'verbose_name_plural': 'Configuraciones de la Biblioteca ',
            },
        ),
        migrations.AddField(
            model_name='libro',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='libroinfantil',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='revista',
            name='factor_estancia',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='revista',
            name='peso',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='libro',
            name='cantidad_prestamo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de prestamo'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='factor_estancia',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='libroinfantil',
            name='cantidad_prestamo',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cantidad de prestamo'),
        ),
        migrations.AlterField(
            model_name='libroinfantil',
            name='factor_estancia',
            field=models.FloatField(default=0),
        ),
    ]