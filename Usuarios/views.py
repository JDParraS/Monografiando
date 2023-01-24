from django.shortcuts import render, get_object_or_404
from .models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import randint as ran
import datetime

from entrys.models import Evento,Year,Modulo
from Usuarios.models import Calificacion

def formEntrar(request):
    return render(request,'Usuarios/formEntrar.html')


def entrar(request):
    try:
        user = get_object_or_404(Usuario,nombre_usuario=request.POST['nombre'],contraseña=request.POST['pw'])
        user.numTemp = ran(0,9999999)
        user.save()
    except:
        return HttpResponse('equivocado')
    
    return HttpResponseRedirect(reverse('PagPrincipal:pag',args=(user.numTemp,)))

def calificaciones(request,numTemp):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0] 
    evens = Evento.objects.all()
    califs = Calificacion.objects.filter(usuario__numTemp=numTemp)
    liEvCal=list()
    for ev in evens:
        fila=list()
        fila.append(ev)
        try:
            calif = califs.filter(evento=ev).order_by('-id')[0]
            fila.append(calif)
        except:
            pass
        liEvCal.append(fila)

    context = {'Usro':Usro,'liEvCal':liEvCal}
    return render(request,'Usuarios/calificaciones.html',context)

def homeworks(request,numTemp):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    evens = Usro.evento.all()
    ids = evens.values_list('id',flat=True)
    evensN = Evento.objects.exclude(id__in=ids)
    context = {'Usro':Usro,'evens':evensN,'ids':ids}
    return render(request,'Usuarios/homeworks.html',context) 
    