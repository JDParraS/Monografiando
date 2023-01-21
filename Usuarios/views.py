from django.shortcuts import render, get_object_or_404
from .models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def formEntrar(request):
    return render(request,'PagPrincipal/base.html')


def entrar(request):
    try:
        global user
        user = get_object_or_404(Usuario,nombre_usuario=request.POST['nombre'],contraseña=request.POST['pw'])
        ctx = {'user':user}
    except:
        return HttpResponse('equivocado')
    
    return render(request,'PagPrincipal/base.html',ctx)

