
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('categoria/<str:titulo>/<int:id>', views.categoria_vista, name='categoria_vista'),
    path('producto/<str:titulo>/<int:id>', views.productos, name = 'productos'),
    path('carta/<int:id>', views.carta, name='carta'),
    path('carro', views.carro, name = 'carro' ),
    path('sobre nosotros', views.carro, name = 'sobre_nosotros' ),
    path('politicas', views.carro, name = 'politicas' ),
    
    #

    path('agregar_al_carrito/<int:product_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar_item_carrito/<int:item_id>/', views.eliminar_item_carrito, name='eliminar_item_carrito'),
    path('eliminar_cantidad_del_carrito/<int:product_id>/', views.eliminar_cantidad_del_carrito, name='eliminar_cantidad_del_carrito'),
    path('obtener_total_carrito/', views.obtener_total_carrito, name='obtener_total_carrito'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)