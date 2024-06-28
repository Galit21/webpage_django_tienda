
from django.urls import path
from . import views


urlpatterns = [
    path('Home', views.home, name='home'),
    path('Herramientas', views.herramientas, name='herramientas'),
    path('Prueba', views.prueba, name='prueba'),

]