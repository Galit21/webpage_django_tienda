from django.shortcuts import render

# Create your views here.

from .models import Producto

def home(request):
    productos = Producto.objects.all()
    context={'productos': productos}
    return render(request, 'tienda/index.html', context)

def prueba(request):
    context={}
    return render(request, 'tienda/prueba.html', context)

def herramientas(request):
    context={}
    return render(request, 'tienda/herramientas.html', context)

def register(request):
    context={}
    return render(request, 'tienda/register.html', context)

def sobre_fundacion(request):
    context={}
    return render(request, 'tienda/sobre_fundación.html', context)

def carta_producto(request):
    context={}
    return render(request, 'tienda/sobre_fundación.html', context)

def categoria(request):
    context={}
    return render(request, 'tienda/sobre_fundación.html', context)