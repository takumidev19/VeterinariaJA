from django.shortcuts import render, get_object_or_404
from gestorProductos.models import Producto, Categoria

# Create your views here.
def productos_list(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'productos/productos.html', {'productos': productos})

def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias.html', {'categorias': categorias})

def productoPorCategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.all()
    return render(request, 'productos/productosPorCategoria.html', {'categoria': categoria, 'productos': productos})