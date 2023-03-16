from django.contrib import admin
from django.urls import path, include

from core.views import inicio, agregar, editar, mostrar, eliminar

urlpatterns = [
    path('', inicio, name="index"),
    path('agregar/', agregar, name="agregar"),
    path('editar/<int:id_curso>/', editar, name="editar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<int:id_curso>/', eliminar, name="eliminar"),
]