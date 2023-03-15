from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'core/index.html')

def agregar(request):
    return render(request, 'core/agregar_curso.html')

def mostrar(request):
    return render(request, 'core/mostrar_curso.html')

def editar(request):
    return render(request, 'core/editar_curso.html')

def eliminar(request):
    return render(request, 'core/eliminar_curso.html')

