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

def carta(request, id):
    categoria = Categoria.objects.all()
    producto = get_object_or_404(Producto, id=id)
    context = {
        'categoria': categoria,
        'producto': producto,
    }
    return render(request, 'tienda/carta_producto.html', context)

def carro(request):
    categoria = Categoria.objects.all()
    itemcarrito = ItemCarrito.objects.all()
    context={
        'categoria': categoria,
        'itemcarrito' : itemcarrito}
    return render(request, 'tienda\carro_compra.html', context)

#-----------------------------------#

def agregar_al_carrito(request, product_id):
    if request.method == 'POST':
        carrito, created = Carrito.objects.get_or_create()
        producto = get_object_or_404(Producto, id=product_id)
        item, created = ItemCarrito.objects.get_or_create(carrito=carrito, producto=producto)
        
        if not created:
            item.cantidad += 1
        item.save()
        
        return JsonResponse({'status': 'success', 'cantidad': item.cantidad})
    
    return JsonResponse({'status': 'error'}, status=400)