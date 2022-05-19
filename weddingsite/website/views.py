from django.shortcuts import render
from .models import Categoria, Foto

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def fotos(request):
    fts = Foto.objects.all()
    context = {
        "fotos": fts,
    }
    return render(request, 'index.html', context)