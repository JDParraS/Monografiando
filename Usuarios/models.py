from django.db import models

# importando otros modelos:

from entrys.models import Year, Contenido, Evento

class Curso(models.Model):
    nombre_curso = models.CharField(max_length=200)
    year = models.ForeignKey(Year,on_delete=models.CASCADE)
    # es endingpoint de Grupo
    # es ending point de Usuario

class Tema(models.Model):
    contenido = models.ManyToManyField(Contenido)
    # es endingpoint de Usuario

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=300)
    nickname = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)
    profesor =models.BooleanField()
    temaInv = models.ForeignKey(Tema,on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    evento = models.ManyToManyField(Evento,through='Calificacion')
    # relacion ManyToMany con Grupo 
    # es endingpoint de Comentario
    # es endingpoint de calificaciones
    # es endingpoint de comentarios
    # es endingpoint de likes
    # es endingpoint de Foro

class Grupo(models.Model):
    curso = models.ForeignKey(Curso,on_delete=models.CASCADE)
    usuarios = models.ManyToManyField(Usuario)
    evento = models.ManyToManyField(Evento,through='Calificacion')
    fechaCreacion = models.DateField()
    # es endingpoint de Calificaciones



class Calificacion(models.Model):
    nota = models.IntegerField()
    fecha = models.DateField()
    evento = models.ForeignKey(Evento,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    grupo = models.ForeignKey(Grupo,on_delete=models.CASCADE)




