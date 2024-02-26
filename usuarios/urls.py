# usuarios/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('actualizar-usuario/<int:usuario_id>/', views.actualizar_usuario, name='actualizar_usuario'),
    path('borrar-usuario/<int:usuario_id>/', views.borrar_usuario, name='borrar_usuario'),
]
