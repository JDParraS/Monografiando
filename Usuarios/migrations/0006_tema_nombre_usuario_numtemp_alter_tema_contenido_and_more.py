# Generated by Django 4.0.7 on 2023-01-21 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrys', '0005_evento_comentariosimple_evento_fecha_and_more'),
        ('Usuarios', '0005_curso_grado'),
    ]

    operations = [
        migrations.AddField(
            model_name='tema',
            name='nombre',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='numTemp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tema',
            name='contenido',
            field=models.ManyToManyField(blank=True, null=True, to='entrys.contenido'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='curso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.curso'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='evento',
            field=models.ManyToManyField(blank=True, null=True, through='Usuarios.Calificacion', to='entrys.evento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='temaInv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Usuarios.tema'),
        ),
    ]