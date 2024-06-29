from django.shortcuts import render

# Create your views here.

from .models import Categoria, SubCategoria

def home(request):
    categoria = Categoria.objects.all()
    context={'categoria': categoria}
    return render(request, 'tienda\index.html', context)

def categoria_vista(request, titulo, id):
    subcategoria = SubCategoria.objects.filter(categoria = id)
    categoria = Categoria.objects.all()
    context={
        'titulo' : titulo,
        'lista_subcategoria' : subcategoria,
        'categoria': categoria
        }
    return render(request, 'tienda\categoria.html', context)

def productos(request):
    categoria = Categoria.objects.all()
    context={'categoria': categoria}
    return render(request, 'tienda\productos.html', context)


