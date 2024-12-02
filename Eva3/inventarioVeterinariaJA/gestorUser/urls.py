from django.urls import path
from . import views
from gestorUser.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/editar/<int:user_id>/', views.editar_usuario, name='editar_usuario'),
    path('eliminar_usuario/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
    
]