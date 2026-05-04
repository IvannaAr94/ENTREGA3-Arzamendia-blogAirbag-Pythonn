from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('crear-post/', views.crear_post, name='crear_post'),
    path('crear-integrante/', views.crear_integrante, name='crear_integrante'),
    path('crear-album/', views.crear_album, name='crear_album'),
    path('integrantes/', views.listar_integrantes, name='listar_integrantes'),
    path('albumes/', views.listar_albumes, name='listar_albumes'),
    path('buscar/', views.buscar_post, name='buscar_post'),
    path('acerca/', views.acerca, name='acerca'),
    path('eliminar-post/<int:id>/', views.eliminar_post, name='eliminar_post'),
]
