from django.contrib import admin

# Register your models here.

from .models import Categoria, SubCategoria, Producto, Carrito, ItemCarrito

admin.site.register(Categoria)
admin.site.register(SubCategoria)
admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)
