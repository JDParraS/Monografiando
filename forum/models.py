from django.db import models
from django.apps import apps

# Modulo = apps.get_model(app_label='entrys',model_name='Modulo')
# Usuario = apps.get_model(app_label='Usuarios',model_name='Usuario')

class Foro(models.Model):
    nombPub = models.CharField(max_length=300)
    textoPub = models.TextField()
    fechaPub = models.DateField()
    usuario = models.ForeignKey('Usuarios.Usuario',on_delete=models.CASCADE)
    # likes = models.ManyToManyField('Usuarios.Usuario',through='Like') →→→→→ DA ERROR YA QUE YA EXISTE UNA 'REFERENCIE AL MISMO MODELO 
    
    # es endingpoint de Contenido
    # es endingpoint de Comentario

class Comentario(models.Model):
    fechaPub = models.DateField()
    foro = models.ForeignKey(Foro,on_delete=models.CASCADE)
    modulo = models.ForeignKey('entrys.Modulo',on_delete=models.CASCADE)
    usuario = models.ForeignKey('Usuarios.Usuario',on_delete=models.CASCADE)
    texto = models.TextField()
    # likes = models.ManyToManyField('Usuarios.Usuario',through='Like')

class Like(models.Model):
    usuario = models.ForeignKey('Usuarios.Usuario',on_delete=models.CASCADE)
    comentario = models.ForeignKey(Comentario,on_delete=models.CASCADE)
    foro = models.ForeignKey(Foro,on_delete=models.CASCADE)
    fecha = models.DateField()
    tipo = models.CharField(max_length=20)


