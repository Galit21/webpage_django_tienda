from django.shortcuts import render

# Create your views here.

from .models import Categoria_index

def home(request):
    categoria_index = Categoria_index.objects.all()
    context={'categoria_index': categoria_index}
    return render(request, 'tienda\index.html', context)

def categoria(request):
    categoria_index = Categoria_index.objects.all()
    context={'categoria_index': categoria_index}
    return render(request, 'tienda\categoria.html', context)

