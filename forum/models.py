from django.db import models
from django.apps import apps
from Usuarios.models import Usuario
from entrys.models import Modulo



class Foro(models.Model):
    nombPub = models.CharField(max_length=300)
    textoPub = models.TextField()
    fechaPub = models.DateField()
    likes = models.ManyToManyField(Usuario,through='Likes')
    
    # es endingpoint de Contenido
    # es endingpoint de Comentario

class Comentario(models.Model):
    fechaPub = models.DateField()
    foro = models.ForeignKey(Foro,on_delete=models.CASCADE)
    modulo = models.ForeignKey(Modulo,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    texto = models.TextField()
    likes = models.ManyToManyField(Usuario,through='Likes')

class Like(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)
    foro = models.ForeignKey(Foro,on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=20)


