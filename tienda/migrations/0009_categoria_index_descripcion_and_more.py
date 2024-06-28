# Generated by Django 4.1.2 on 2024-06-28 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0008_alter_categoria_index_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria_index',
            name='descripcion',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='categoria_index',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]