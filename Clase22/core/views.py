from django.shortcuts import render
from core.models import Curso
from core.forms import CursoForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

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

# VISTAS BASADAS EN CLASES
class CursoListView(ListView):
    model = Curso
    template_name = 'core/mostrar_view.html'

    def get(self, request, *args, **kwargs):
        print("\n\n\n\nMI PRINT\n\n\n\n")
        return super().get(request, *args, **kwargs)
    
class CursoDetailView(DetailView):    
    model = Curso
    template_name = 'core/curso_detalle_view.html'

class CursoDeleteView(DeleteView):
    model = Curso
    # AGREGADO
    template_name = 'core/curso_confirm_del_view.html'
    success_url = '/core/mostrar_view/'

class CursoCreateView(CreateView):
    model = Curso
    template_name = 'core/curso_form_view.html'
    success_url = '/core/mostrar_view/'
    fields = ['nombre', 'camada']

class CursoUpdateView(UpdateView):
    model = Curso
    # AGREGADO
    template_name = 'core/curso_form_view.html'
    success_url = '/core/mostrar_view/'
    fields = ['id', 'nombre']


