# Generated by Django 4.1.2 on 2024-06-29 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0017_subcategoria_delete_subcategorias'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
