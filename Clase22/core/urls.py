from django.contrib import admin
from django.urls import path, include

from core.views import inicio, agregar, editar, mostrar, eliminar

urlpatterns = [
    path('', inicio, name="index"),
    path('agregar/', agregar, name="agregar"),
    path('editar/', editar, name="editar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/', eliminar, name="eliminar"),

]