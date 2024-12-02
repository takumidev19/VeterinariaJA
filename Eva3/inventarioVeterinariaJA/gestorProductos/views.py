from django.shortcuts import render, get_object_or_404, redirect
from gestorProductos.models import Producto, Categoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseForbidden

def productos_list(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'productos/productos.html', {'productos': productos})

@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria_id = request.POST['categoria']
        categoria = get_object_or_404(Categoria, id=categoria_id)

        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            usuario=request.user
        )
        return redirect('productos_list')

    categorias = Categoria.objects.all()
    return render(request, 'productos/crear_producto.html', {'categorias': categorias})

@login_required
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        categoria_id = request.POST['categoria']
        categoria = get_object_or_404(Categoria, id=categoria_id)
        producto.categoria = categoria
        producto.save()

        return redirect('productos_list')

    categorias = Categoria.objects.all()
    return render(request, 'productos/editar_producto.html', {'producto': producto, 'categorias': categorias})

@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()
        return redirect('productos_list')

    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

def productoPorCategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.all()
    return render(request, 'productos/productosPorCategoria.html', {'categoria': categoria, 'productos': productos})

def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias.html', {'categorias': categorias})

@login_required
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = Categoria.objects.create(nombre=nombre)

        messages.success(request, "Categoría creada correctamente.")

        return redirect('categorias_list')
    
    return render(request, 'categorias/crear_categoria.html')

@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('categorias_list')
    
    return render(request, 'categorias/editar_categoria.html', {'categoria': categoria})

@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias_list')

    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})




