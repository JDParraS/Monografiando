from django.urls import path

from . import views
app_name = 'Usuarios'
urlpatterns = [
    path('',views.formEntrar, name = 'formEntrar' ),
    path('entrar',views.entrar, name = 'entrar'),
]