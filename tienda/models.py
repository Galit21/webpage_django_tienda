from django.db import models

# Create your models here.

class Categoria_index(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    imagen = models.FileField(upload_to='categoria/')
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.nombre
