# Generated by Django 4.0.7 on 2023-01-23 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrys', '0011_ejercicio_formtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='tipo',
            field=models.CharField(choices=[('Respuesta Multiple', 'Respuesta Multiple'), ('Respuesta Unica', 'Respuesta Unica'), ('Texto', 'Texto')], max_length=100),
        ),
    ]
