# Generated by Django 4.2.7 on 2024-08-06 19:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "biblioteca",
            "0002_alter_concurso_categorias_alter_concurso_descrpcion_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="asistencia",
            name="horas",
            field=models.IntegerField(default=0, verbose_name="Horas Trabajadas"),
            preserve_default=False,
        ),
    ]
