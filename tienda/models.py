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