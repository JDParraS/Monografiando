from django.shortcuts import render, get_object_or_404
from .models import Usuario
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from random import randint as ran
import datetime

from entrys.models import Evento,Year,Modulo
from Usuarios.models import Calificacion,Tema,Curso

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

def formCrear(request):
    curs = Curso.objects.all()
    tems = Tema.objects.all()
    context={'curs':curs,'tems':tems}
    return render(request,'Usuarios/crearCuenta.html',context)

def crear(request):
    nombre = request.POST['nombre']
    nickname = request.POST['nick']
    contraseña = request.POST['pw']
    temaInv = Tema.objects.get(id=request.POST['TemaInv'])
    curso = Curso.objects.get(id=request.POST['Curso'])
    Usuario.objects.create(nombre_usuario=nombre,nickname=nickname,contraseña=contraseña,temaInv=temaInv,curso=curso)
    return HttpResponseRedirect(reverse('Usuarios:formEntrar'))

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
    