# Generated by Django 4.1.2 on 2024-06-28 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_categoria_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categoria_herramientas',
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
