from django.urls import path
from . import views

app_name = 'PagPrincipal'
urlpatterns = [
    path('<int:numTemp>',views.pag, name = 'pag' ),
]