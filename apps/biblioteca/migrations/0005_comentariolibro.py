# Generated by Django 4.2.7 on 2025-04-19 23:39

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_alter_archivo_user_alter_usuarioseventuales_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioLibro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField(validators=[django.core.validators.RegexValidator('^[0-9a-zA-ZáéíóúÁÉÍÓÚñÑ ,.!¡¿?]+$')], verbose_name='Comentario')),
                ('puntuacion', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='La puntuación mínima es 1'), django.core.validators.MaxValueValidator(5, message='La puntuación máxima es 5')], verbose_name='Puntuación')),
                ('fecha', models.DateTimeField(auto_now_add=True, verbose_name='Fecha')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.libro', verbose_name='Libro')),
                ('suscriptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='biblioteca.suscriptor', verbose_name='Suscriptor')),
            ],
            options={
                'verbose_name': 'Comentario de Libro',
                'verbose_name_plural': 'Comentarios de Libros',
                'unique_together': {('libro', 'suscriptor')},
            },
        ),
    ]
