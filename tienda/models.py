from django.db import models

# Create your models here.

class Categoria(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.FileField(upload_to='categoria/')
    def __str__(self):
        return self.nombre

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    imagen = models.FileField(upload_to='subcategoria/')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    valor = models.IntegerField(max_length=10)
    imagen = models.FileField(upload_to='producto/')
    subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
        
class Carrito(models.Model):
    creado = models.DateTimeField(auto_now_add=True)

class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def str(self):
        return f'{self.producto.nombre} x {self.cantidad}'