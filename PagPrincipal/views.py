from django.shortcuts import render
from django.http import HttpResponse

def pag(request):
    return HttpResponse('hola que tal')