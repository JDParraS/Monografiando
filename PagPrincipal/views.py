from django.shortcuts import render
from django.http import HttpResponse
from Usuarios.models import Usuario
from entrys.models import Modulo,Year,Semana,Evento

def pag(request,numTemp):
    Usro = Usuario.objects.filter(numTemp=numTemp)[0]
    lstModSemEv=list()
    mods = Modulo.objects.filter(year__year=2023)
    for i in mods:
        lstFila =list()
        lstFila.append(i)
        lstFila.append(Semana.objects.filter(modulo=i)[0])
        lstFila.append(Evento.objects.filter(semana=lstFila[1]))
        lstModSemEv.append(lstFila)
    context = {'Usro':Usro,'Resumen':lstModSemEv}
    return render(request,'PagPrincipal/index.html',context)