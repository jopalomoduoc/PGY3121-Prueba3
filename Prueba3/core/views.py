from django.shortcuts import render
from .models import Libro

# Create your views here.
def home(request):
    return render(request, 'core/home.html')
def libro_lista(request):
    libros = Libro.objects.all()
    datos = {
        'libros' : libros
     }
    return render(request, 'core/libro_lista.html', datos)

def libro_form(request):
     return render(request, 'core/form_libro')   