# Generated by Django 4.0.7 on 2023-01-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0003_tema_contenido_grupo_curso_grupo_evento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='nombre',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
