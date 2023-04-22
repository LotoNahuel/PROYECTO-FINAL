from django.shortcuts import render
from .models import *
from .forms import *
from django.db.models import Q
from django.http import HttpResponse
#---#
from django.contrib.auth.forms import  UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required #para vistas basadas en funciones DEF  

# Create your views here.

def inicio(request):
    return render(request, "inicio.html")

def diseños(request):
    if request.method == "POST":
        form = DiseñoForm(request.POST)
        if form.is_valid():
            diseño = Diseño()
            diseño.titulo = form.cleaned_data["titulo"]
            diseño.diseño = form.cleaned_data["diseño"]
            diseño.descripcion = form.cleaned_data["descripcion"]
            diseño.fechaPost = form.cleaned_data["fechaPost"]
            diseño.emailUsuario = form.cleaned_data["emailUsuario"]
            diseño.save()
            form = DiseñoForm()
    else:
        form = DiseñoForm()

    diseños = Diseño.objects.all()
    context = {"diseños": diseños, "form": form}
    return render(request, "padre.html", context)

    
def otroFilter(request):
    diseño = request.GET["diseño"]
    if "Otr" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Otro").all
        return render(request, "filtroLista.html", {"diseños": diseños})
    
def arteFilter(request):
    diseño = request.GET["diseño"]
    if "Arte" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Arte").all
        return render(request, {"diseños": diseños})
    
def modaFilter(request):
    diseño = request.GET["diseño"]
    if "Moda" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Moda").all
        return render(request, {"diseños": diseños})
    
def joyaFilter(request):
    diseño = request.GET["diseño"]
    if "Joyas" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Joyas").all
        return render(request, {"diseños": diseños})

def casaFilter(request):
    diseño = request.GET["diseño"]
    if "Casa" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Casa").all
        return render(request, {"diseños": diseños})
    
def arquitecturaFilter(request):
    diseño = request.GET["diseño"]
    if "Arquitectura" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Arquitectura").all
        return render(request, {"diseños": diseños})
    
def artilugioFilter(request):
    diseño = request.GET["diseño"]
    if "Artilugio" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Artilugio").all
        return render(request, {"diseños": diseños})
    
def juegoFilter(request):
    diseño = request.GET["diseño"]
    if "Juego" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Juego").all
        return render(request, {"diseños": diseños})

def herramientaFilter(request):
    diseño = request.GET["diseño"]
    if "Herramienta" in diseño:
        diseños = Diseño.objects.filter(diseño__icontains="Herramienta").all
        return render(request, {"diseños": diseños}) 

#RegisterAndLogin

def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info=form.cleaned_data

            usuary=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usuary, password=clave)

            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html", {"mensaje":f"Usuario {usuary} logueado correctamente"})
            else:
                return render(request, "login.html", {"form": form, "mensaje":"Usuario y/o contraseña incorrectos"})
        else:
            return render(request, "login.html", {"form": form, "mensaje":"Usuario y/o contraseña incorrectos"})
    else:
        form=AuthenticationForm()
        return render(request, "login.html", {"form": form})


def register(request):
    if request.method=="POST":
        form= RegistroForm(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render(request, "inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "register.html", {"form": form, "mensaje":"Error al crear el usuario"})
    else:
        form= RegistroForm()
        return render(request, "AppCoder/register.html", {"form": form})