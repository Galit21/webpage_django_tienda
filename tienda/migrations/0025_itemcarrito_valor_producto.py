# Generated by Django 4.1.2 on 2024-06-30 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0024_carrito_itemcarrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemcarrito',
            name='valor_producto',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
