from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscar_articulo, name='inicio'),
    path('autor/', views.crear_autor, name='crear_autor'),
    path('articulo/', views.crear_articulo, name='crear_articulo'),
    path('comentario/', views.crear_comentario, name='crear_comentario'),
    path('buscar/', views.buscar_articulo, name='buscar_articulo'),
]
