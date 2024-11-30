from django.urls import path
from .views import productoPorCategoria

urlpatterns = [
    path('categoria/<int:categoria_id>/productos/', productoPorCategoria, name='productosPorCategoria'),
]
