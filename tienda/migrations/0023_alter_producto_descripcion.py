# Generated by Django 4.1.2 on 2024-06-29 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0022_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=500),
        ),
    ]
