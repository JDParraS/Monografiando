from rest_framework import viewsets, permissions
from Usuarios.models import  Calificacion
from .serializers import ProjectSerializer

class interviewViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class= ProjectSerializer