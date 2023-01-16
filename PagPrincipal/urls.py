from django.urls import path

from . import views
app_name = 'PagPrincipal'
urlpatterns = [
    path('',views.pag, name = 'pag' ),
]