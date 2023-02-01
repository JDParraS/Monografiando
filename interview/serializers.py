from rest_framework import serializers
from Usuarios.models import  Calificacion

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Calificacion
        fields = ('nota','fecha','evento','usuario','grupo')
        read_only_fields = ('usuario',)