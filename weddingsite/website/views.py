from django.shortcuts import render
from .models import Categoria, Foto

# Create your views here.
def inicio(request):
    return render(request, 'inicio.html')


def nosotros(request):
    return render(request, 'nosotros.html')


def galeria(request):
    return render(request, 'galeria.html')