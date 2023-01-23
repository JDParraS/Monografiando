from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from Usuarios.models import Usuario,Calificacion
from entrys.models import Modulo,Year,Semana,Evento,Contenido,Ejercicio,Opciones

def verModulo(request,numTemp,numMod):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    mod = Modulo.objects.get(pk=numMod)
    sems = Semana.objects.filter(modulo=mod)
    sems.order_by('seman')
    context={'mod':mod,'sems':sems,'Usro':Usro}
    return render(request,'entrys/modulos.html',context)

def verSemana(request,numTemp,numMod,numSem):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    mod = Modulo.objects.get(pk=numMod)
    sem = Semana.objects.get(pk=numSem,modulo=mod)
    evens = Evento.objects.filter(semana=sem)
    context = {'mod':mod,'sem':sem,'Usro':Usro,'evens':evens}
    return render(request,'entrys/semanas.html',context)

def verEvento(request,numTemp,numMod,numSem,numEven):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    mod = Modulo.objects.get(pk=numMod)
    sem = Semana.objects.get(pk=numSem,modulo=mod)
    even = Evento.objects.get(id=numEven)
    cdos = even.contenidos.all()
    ejs = Ejercicio.objects.filter(evento=even)
    calif = Calificacion.objects.filter(evento=even,usuario=Usro) 
    lstEjs = list()
    for i in ejs:
        lstOps=list()
        lstOps.append(i)
        lstOps.append(Opciones.objects.filter(ejercicio=i))
        lstEjs.append(lstOps)
    context = {'mod':mod,'sem':sem,'Usro':Usro,'even':even,'cdos':cdos,'lstEjOp':lstEjs,'calif':calif}
    return render(request,'entrys/entrada.html',context)

def evaluador(request,numTemp,numMod,numSem,numEven):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    mod = Modulo.objects.get(pk=numMod)
    sem = Semana.objects.get(pk=numSem,modulo=mod)
    even = Evento.objects.get(id=numEven)
    cdos = even.contenidos.all()
    ejs = Ejercicio.objects.filter(evento=even)
    calif = Calificacion.objects.filter(evento=even,usuario=Usro) 
    lstEjs = list()
    for i in ejs:
        lstOps=list()
        lstOps.append(i)
        lstOps.append(Opciones.objects.filter(ejercicio=i))
        lstEjs.append(lstOps)
    return HttpResponseRedirect(reverse('entrys:verEvento',args=(numTemp,numMod,numSem,numEven)))