# Generated by Django 4.0.7 on 2023-01-16 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0002_calificacion_curso_grupo_tema_usuario_evento'),
        ('entrys', '0003_contenido_ejercicio_modulo_year_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPub', models.DateField()),
                ('texto', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Foro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombPub', models.CharField(max_length=300)),
                ('textoPub', models.TextField()),
                ('fechaPub', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo', models.CharField(max_length=20)),
                ('comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.comentario')),
                ('foro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.foro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='foro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.foro'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='modulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='entrys.modulo'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario'),
        ),
    ]
