from django.shortcuts import render
from core.models import Curso
from core.forms import CursoForm

# Create your views here.
def inicio(request):
    return render(request, 'core/index.html')

def agregar(request):

    if request.method == "POST":

        curso_form = CursoForm(request.POST)

        if curso_form.is_valid():
            data = curso_form.cleaned_data
            curso = Curso(nombre=data["name"], camada=data["n_camada"])
            curso.save()
            return render(request, 'core/index.html')

    curso_form = CursoForm()

    return render(request, 'core/agregar_curso.html', {"form": curso_form})

def mostrar(request):

    cursosx = Curso.objects.all()

    return render(request, 'core/mostrar_curso.html', {"cursos": cursosx})

def editar(request, id_curso):

    curso = Curso.objects.get(id=id_curso)

    if request.method == "POST":
        curso_form = CursoForm(request.POST)
        if curso_form.is_valid():
            data = curso_form.cleaned_data
            curso.nombre = data["name"]
            curso.camada = data["n_camada"]
            curso.save()
            return render(request, 'core/index.html')
    else:
        # Mediante método GET
        curso_form = CursoForm(initial={'name': curso.nombre, 'n_camada': curso.camada})
        
        return render(request, 'core/editar_curso.html', {'form': curso_form})

def eliminar(request, id_curso):

    curso = Curso.objects.get(id=id_curso)
    name = curso.nombre
    curso.delete()

    return render(request, 'core/eliminar_curso.html', {"nombre_eliminado": name})

