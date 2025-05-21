from django.urls import path
from . import views

urlpatterns = [
    path('', views.agregar_maquina, name='agregar_maquina'),
]