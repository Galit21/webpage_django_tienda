# Generated by Django 4.1.2 on 2024-06-29 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0015_alter_subcategorias_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]