from django.shortcuts import render, get_object_or_404
from .models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import randint as ran

def formEntrar(request):
    return render(request,'Usuarios/formEntrar.html')


def entrar(request):
    try:
        user = get_object_or_404(Usuario,nombre_usuario=request.POST['nombre'],contraseña=request.POST['pw'])
        user.numTemp = ran(0,9999999999999)
        user.save()
    except:
        return HttpResponse('equivocado')
    
    return HttpResponseRedirect(reverse('PagPrincipal:pag',args=(user.numTemp,)))

    