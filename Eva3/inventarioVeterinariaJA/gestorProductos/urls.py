from django.urls import path
from . import views

urlpatterns = [
    path('categorias/', views.categorias_list, name='categorias_list'),
    path('categorias/crear/', views.crear_categoria, name='crear_categoria'),
    path('categorias/editar/<int:categoria_id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/eliminar/<int:categoria_id>/', views.eliminar_categoria, name='eliminar_categoria'),
    path('categoria/<int:categoria_id>/productos/', views.productoPorCategoria, name='productosPorCategoria'),
    path('productos/', views.productos_list, name='productos_list'), 
    path('productos/crear/', views.crear_producto, name='crear_producto'), 
    path('productos/editar/<int:producto_id>/', views.editar_producto, name='editar_producto'), 
    path('productos/eliminar/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'), 
    path('categoria/<int:categoria_id>/productos/', views.productoPorCategoria, name='productosPorCategoria'),
]
