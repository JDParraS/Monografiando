from django.db import models
from django.apps import apps

# Foro = apps.get_model(app_label='forum',model_name='Foro')

class Year(models.Model):
    year = models.IntegerField()
    # es endingpoint de Curso
    # es endingpoint de Modulo

class Modulo(models.Model):
    tituloMod = models.CharField(max_length=300)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    # es endingpoint de Foro
    # es endingpoint de Semana

class Semana (models.Model):
    tituloSem = models.CharField(max_length=300)
    seman = models.IntegerField()
    modulo = models.ForeignKey(Modulo, on_delete=models.CASCADE)
    # es endingpoint de Evento

class Contenido(models.Model):
    tipo = models.CharField(max_length=100)
    ubic = models.CharField(max_length=200)
    foro = models.ForeignKey('forum.Foro',on_delete=models.CASCADE)
    # es endingpoint ManyToMany de Tema
    # es endingpoint ManyToMany de Evento

class Evento(models.Model):
    nombre = models.CharField(max_length=300)
    semana = models.ForeignKey(Semana,on_delete=models.CASCADE)
    contenidos = models.ManyToManyField(Contenido)
    comentario = models.TextField()
    # es el endpoint de ejercicios
    # es endpoint de calificacion
    # es el endpoint de ManyToMany de Grupo
    # es el endpoint de ManyToMany de Usuario

class Ejercicio(models.Model):
    tipo = models.CharField(max_length=100)
    puntaje = models.IntegerField()
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    # es endingpoint de Opciones

class Opciones(models.Model):
    opcion = models.CharField(max_length=1000)
    correcta = models.BooleanField()
    ejercicio = models.ForeignKey(Ejercicio,on_delete=models.CASCADE)