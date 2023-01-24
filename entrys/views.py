from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from Usuarios.models import Usuario,Calificacion
from entrys.models import Modulo,Year,Semana,Evento,Contenido,Ejercicio,Opciones
import re


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

def verEvento(request,numTemp,numEven):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    even = Evento.objects.get(id=numEven)
    cdos = even.contenidos.all()
    ejs = Ejercicio.objects.filter(evento=even)
    try:
        calif = Calificacion.objects.filter(evento=even,usuario=Usro).order_by('-id')[0]
    except:
        calif=None
    lstEjs = list()
    for i in ejs:
        lstOps=list()
        lstOps.append(i)
        lstOps.append(Opciones.objects.filter(ejercicio=i))
        lstEjs.append(lstOps)
    context = {'Usro':Usro,'even':even,'cdos':cdos,'lstEjOp':lstEjs,'calif':calif}
    return render(request,'entrys/entrada.html',context)

def evaluador(request,numTemp,numEven):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    even = Evento.objects.get(id=numEven)
    ejs = Ejercicio.objects.filter(evento=even)
    calif=0.0
    punTot = 0
    for ej in ejs:
        punTot = punTot+ej.puntaje
        opcs = ej.opciones_set.all()

        if ej.formType=='radio':
            try:
                opcionEsc = opcs.get(id=request.POST['Ej'+str(ej.id)])
            except:
                continue
            if opcionEsc.correcta==True:
                calif=calif+ej.puntaje
            continue
        
        

        elif ej.formType=='checkbox':
            opcsCor = opcs.filter(correcta=True)
            valorOp = ej.puntaje/opcsCor.count()
            for opc in opcsCor: 
                try:
                    if str(opc.id) == request.POST['Op'+str(opc.id)]:
                        calif=calif+valorOp
                except:
                    pass
            continue
        
        elif ej.formType=='text':
            if len(request.POST['Ej'+str(ej.id)])>0:
                calif = calif+ej.puntaje

    try:
        calif = round(calif/punTot*5,2)
    except:
        calif= 5
    clifObj = Calificacion.objects.create(nota=calif,evento=even,usuario=Usro)
    clifObj.save()
    return HttpResponseRedirect(reverse('entrys:verEvento',args=(numTemp,numEven)))