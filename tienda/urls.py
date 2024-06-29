
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:titulo>/<int:id>', views.categoria_vista, name='categoria_vista'),
    path('productos', views.productos, name = 'productos')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)