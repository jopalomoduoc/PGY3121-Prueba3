from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')


def libro_lista(request):
    libros = Libro.objects.all()
    datos = {
        'libros': libros
     }
    return render(request, 'core/libro_lista.html', datos)


def form_libro(request):
    datos = {
        'form': LibroForm()
    }
    if request.method == 'POST':
        formulario = LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            formulario = LibroForm()
            datos['mensaje'] = "Datos Ingresados correctamente"
        else:
            datos['mensaje'] = "ISBN Incorrecto"
    return render(request, 'core/form_libro.html', datos)


def form_mod_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    datos = {
        'form': LibroForm(instance=libro)
    }
    if request.method == 'POST':
        formulario = LibroForm(data=request.POST, instance=libro)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado correctamente"
    return render(request, 'core/form_mod_libro.html', datos)

def form_del_libro(request, id):
    libro = Libro.objects.get(ISBN=id)
    libro.delete()
    return redirect(to="libro_lista")


