from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from tienda.models import Producto
import datetime

# Create your views here.

from .models import Categoria, SubCategoria, Producto, Carrito, ItemCarrito

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

def productos(request, id, titulo):
    categoria = Categoria.objects.all()
    subcategoria = SubCategoria.objects.all()
    lista_producto = Producto.objects.filter(subcategoria = id)
    context={
        'categoria': categoria,
        'subcategoria': subcategoria,
        'lista_producto' : lista_producto,
        'titulo' : titulo
        }
    return render(request, 'tienda\productos.html', context)

def carta(request, titulo, id):
    categoria = Categoria.objects.all()
    producto = Producto.objects.get(id = id)
    titulo = producto.nombre
    context={
        'categoria': categoria,
        'titulo' : titulo,
        'producto' : producto
        }
    return render(request, 'tienda\carta_producto.html', context)

def carro(request):
    categoria = Categoria.objects.all()
    context={'categoria': categoria}
    return render(request, 'tienda\carro_compra.html', context)
#-----------------------------------#

