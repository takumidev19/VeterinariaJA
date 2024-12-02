from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden

@login_required
def index(request):
    return render(request, 'index.html')

def usuarios_list(request):
    usuarios = User.objects.all()
    return render(request, 'usuarios/usuarios.html', {'usuarios': usuarios})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    if request.user != usuario and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para editar este usuario.")

    if request.method == 'POST':
        if request.user.is_superuser:
            usuario.username = request.POST.get('username')
            usuario.email = request.POST.get('email')
        else:
            usuario.username = request.POST.get('username')
            usuario.email = request.POST.get('email')

        usuario.save()
        messages.success(request, "Usuario editado correctamente.")

        return redirect('index')

    return render(request, 'usuarios/editar_usuario.html', {'usuario': usuario})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')

    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})   
