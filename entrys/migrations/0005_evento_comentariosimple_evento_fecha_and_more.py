# Generated by Django 4.0.7 on 2023-01-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrys', '0004_contenido_foro_evento_contenidos_alter_evento_semana'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='comentarioSimple',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='evento',
            name='fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ejercicio',
            name='tipo',
            field=models.CharField(choices=[('ResMult', 'ResMult'), ('ResUni', 'ResUni')], max_length=100),
        ),
        migrations.AlterField(
            model_name='evento',
            name='contenidos',
            field=models.ManyToManyField(blank=True, null=True, to='entrys.contenido'),
        ),
    ]
