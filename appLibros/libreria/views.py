from django.shortcuts import render, redirect
from .models import libro
from .forms import LibroForm

# Create your views here.

# ACCESO AL SITIO
def inicio(request):
    return render(request,"paginas/inicio.html")

def nosotros(request):
    return render(request,"paginas/nosotros.html")

#LIBROS
def libros(request):
    libros = libro.objects.all()
    return render(request,"libros/index.html",{"libros":libros})

def crearLibro(request):
    form = LibroForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect("libros")
    return render(request,"libros/crear.html",{"form":form})

def editarLibro(request):
    return render(request,"libros/editar.html")