from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=300)
    tipo = models.CharField(max_length=300)
    semana = models.IntegerField()
    # es el endpoint de ejercicios
    contenidos =[('pdf','pdf'),('video','video'),('plainText','plainTExt')]
    contenido = models.CharField(max_length=20, choices=contenidos,default='video')

    comentario = models.TextField()

