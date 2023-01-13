from django.shortcuts import render
from .models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def formEntrar(request):
    return render(request,'Usuarios/entrar.html')

def entrar(request):
    nombreU = request.POST['nombre']
    pww = request.POST['pw']
    u = Usuario.objects.get(nombre_usuario=nombreU,contraseña = pww)
    return HttpResponseRedirect(reverse(''))

