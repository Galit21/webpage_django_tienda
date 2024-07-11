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

def sobre_nosotros(request):
    categoria = Categoria.objects.all()
    context={'categoria': categoria}
    return render(request, 'tienda\sobre_nosotros.html', context)

def politicas(request):
    categoria = Categoria.objects.all()
    context={'categoria': categoria}
    return render(request, 'tienda\politicas.html', context)

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

def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    try:
        item.delete()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def eliminar_cantidad_del_carrito(request, product_id):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        item = get_object_or_404(ItemCarrito, producto__id=product_id)
        if item.cantidad > 0:
            item.cantidad -= 1
            item.save()
            data = {
                'status': 'success'
            }
        else:
            data = {
                'status': 'error',
                'message': 'No se puede reducir la cantidad.'
            }
    else:
        data = {
            'status': 'error',
            'message': 'La solicitud no es válida.'
        }
    return JsonResponse(data)

def obtener_total_carrito(request):
    if request.method == 'GET':
        carrito = get_object_or_404(Carrito)
        total = sum(item.cantidad * item.valor_producto for item in carrito.items.all())
        return JsonResponse({'total': total})