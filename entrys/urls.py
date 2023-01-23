from django.urls import path
from . import views

app_name = 'entrys'
urlpatterns = [
    path('<int:numTemp>/<int:numMod>',views.verModulo, name = 'verModulo' ),
    path('<int:numTemp>/<int:numMod>/<int:numSem>',views.verSemana, name='verSemana'),
    path('<int:numTemp>/<int:numMod>/<int:numSem>/<int:numEven>',views.verEvento,  name='verEvento'),
    path('/eval/<int:numTemp>/<int:numMod>/<int:numSem>/<int:numEven>',views.evaluador,name='evaluador')
]