from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from tienda.models import Producto
import datetime

# Create your views here.

from .models import Categoria, SubCategoria, Producto, Carrito, ItemCarrito, Usuario

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

def registro(request):
    categoria = Categoria.objects.all()
    context={'categoria': categoria}
    return render(request, 'tienda\crear_registro.html', context)

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

def eliminar_item_carrito(request, item_id):
    item = get_object_or_404(ItemCarrito, id=item_id)
    try:
        item.delete()
        return JsonResponse({'status': 'success'})
    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)})

def eliminar_cantidad_carrito(request, product_id):
    if request.method == 'POST':
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        producto = get_object_or_404(Producto, id=product_id)

        try:
            item = ItemCarrito.objects.get(carrito=carrito, producto=producto)
            if item.cantidad > 1:
                item.cantidad -= 1
                item.save()
                return JsonResponse({'status': 'success', 'cantidad': item.cantidad})
            else:
                item.delete()
                return JsonResponse({'status': 'success', 'cantidad': 0})
        except ItemCarrito.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Producto no encontrado en el carrito'})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)


def calcular_total_carrito(request):
    if request.method == 'GET':
        carrito, created = Carrito.objects.get_or_create(usuario=request.user)
        total = sum(item.cantidad * item.valor_producto for item in carrito.itemcarrito_set.all())
        return JsonResponse({'status': 'success', 'total': total})
    return JsonResponse({'status': 'error', 'message': 'Método no permitido'}, status=405)


#-----------------------------------------------------#
@csrf_protect
def registrar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        contrasena = request.POST.get('contrasena')
        
        try:
            nuevo_usuario = Usuario(nombre=nombre, apellido=apellido, email=email, contrasena=contrasena)
            nuevo_usuario.full_clean()  # Realiza todas las validaciones del modelo
            nuevo_usuario.save()
            return JsonResponse({'status': 'success'})
        
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': 'Ocurrió un error al guardar el usuario.'})

    return JsonResponse({'status': 'error', 'message': 'Método de solicitud no permitido'})