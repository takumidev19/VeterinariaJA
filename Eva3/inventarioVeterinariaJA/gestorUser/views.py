from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from rest_framework.reverse import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden

# Create your views here.
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
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.is_active = 'is_active' in request.POST
        user.is_superuser = 'is_superuser' in request.POST
        user.save()
        return redirect('usuarios_list')  # Redirigir a la lista de usuarios después de editar

    return render(request, 'usuarios/editar_usuario.html', {'user': user})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(User, id=usuario_id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios_list')  # Redirige a la lista de usuarios después de eliminar

    return render(request, 'usuarios/eliminar_usuario.html', {'usuario': usuario})   
