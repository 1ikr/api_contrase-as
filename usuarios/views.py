# usuarios/views.py
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Usuario
import json

def crear_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        nuevo_usuario = Usuario.objects.create(
            nombre=data['nombre'],
            contraseña=data['contraseña']
        )
        return JsonResponse({'mensaje': 'Usuario creado correctamente'}, status=201)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def actualizar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'PUT':
        data = json.loads(request.body)
        usuario.contraseña = data['contraseña']
        usuario.save()
        return JsonResponse({'mensaje': 'Contraseña de usuario actualizada correctamente'}, status=200)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)

def borrar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, pk=usuario_id)
    if request.method == 'DELETE':
        usuario.delete()
        return JsonResponse({'mensaje': 'Usuario eliminado correctamente'}, status=200)
    else:
        return JsonResponse({'mensaje': 'Método no permitido'}, status=405)
