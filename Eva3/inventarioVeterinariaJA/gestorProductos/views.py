from django.shortcuts import render
from gestorProductos.models import Producto, Categoria

# Create your views here.
def productos_list(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'productos.html', {'productos': productos})

def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})