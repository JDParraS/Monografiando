# Generated by Django 4.0.7 on 2023-01-21 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0004_grupo_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='grado',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
