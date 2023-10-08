from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_publicaciones, name='listar_publicaciones'),
    path('crear/', views.crear_publicacion, name='crear_publicacion'),
    path('<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),
]

