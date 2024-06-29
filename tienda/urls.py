
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


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)