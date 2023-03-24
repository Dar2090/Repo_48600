from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from perfil.forms import UserRegisterForm
# Create your views here.

def login_request(request):
    msj = ""
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contra)

            if user:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return render(request, 'core/index.html')
            else:
                msj = "ERROR DE USUARIO"
        else:
            msj = "ERROR DE FORMULARIO"
    
    form = AuthenticationForm()
    return render(request, "perfil/login.html", {"form": form, "msj": msj})

def register(request):
    msj = "CREANDO USUARIO"
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "core/index.html", {"msj": f"Bienvenido {username}"})
        else:
            msj = "ERROR CREANDO USUARIO"
    
    form = UserRegisterForm()
    return render(request, "perfil/registro.html", {"form": form, "msj": msj})