# Generated by Django 4.2.7 on 2024-12-15 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0017_archivo'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='devolucion',
            field=models.BooleanField(default=False),
        ),
    ]
