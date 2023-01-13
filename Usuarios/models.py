from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=300)
    nickname = models.CharField(max_length=100)
    contraseña = models.CharField(max_length=100)

    # es endingpoint de calificacion

    #curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    #grupo = models.models.ManyToManyField(
    # # #     Grupo,
    # # #     through='GrupoUsuario',
    # # #     through_fields=('grupo', 'persona'),
    # # # )
    ## SE CREA OTRA CLASE
    # #class GupoUsuario(models.Model):
    # # # grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    # # # person = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # # # inviter = models.ForeignKey(
    # # #     Person,
    # # #     on_delete=models.CASCADE,
    # # #     related_name="membership_invites",
    # # # )

    # es endpoint de Comentario

    #comentario = models.models.ManyToManyField(
    # # #     Usuario,
    # # #     through='Likes',
    # # #     through_fields=('comentario', 'usuario'),
    # # # )
    ## SE CREA OTRA CLASE
    # #class Likes(models.Model):
    # # # comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    # # # usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    # # # inviter = models.ForeignKey(
    # # #     Person,
    # # #     on_delete=models.CASCADE,
    # # #     related_name="membership_invites",
    # # # )

    # curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
   
    profesor =models.BooleanField()
   
    # tema = models.ForeignKey(Tema,on_delete=models.CASCADE)
