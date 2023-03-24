from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from core.views import inicio, agregar, editar, mostrar, eliminar
from core.views import CursoListView, CursoCreateView, CursoDeleteView, CursoDetailView, CursoUpdateView

urlpatterns = [
    path('', inicio, name="index"),
    path('agregar/', agregar, name="agregar"),
    path('editar/<int:id_curso>/', editar, name="editar"),
    path('mostrar/', mostrar, name="mostrar"),
    path('eliminar/<int:id_curso>/', eliminar, name="eliminar"),
]

# URL's de vistas basadas en Clase
urlpatterns += [
    path('mostrar_view/', CursoListView.as_view(), name='mostrar_view'),
    path('borrar/<pk>/', CursoDeleteView.as_view(), name='delete_view'),
    path('nuevo/', CursoCreateView.as_view(), name='new_view'),
    path('<pk>/', CursoDetailView.as_view(), name='detalle_view'),
    path('editar_view/<pk>/', CursoUpdateView.as_view(), name='edit_view'),
]
