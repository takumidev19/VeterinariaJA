from django.shortcuts import render, get_object_or_404, redirect
from gestorProductos.models import Producto, Categoria
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

# Vista para listar los productos
def productos_list(request):
    if request.user.is_superuser:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(usuario=request.user)
    return render(request, 'productos/productos.html', {'productos': productos})

# Vista para crear un producto
@login_required
def crear_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        categoria_id = request.POST['categoria']
        categoria = get_object_or_404(Categoria, id=categoria_id)

        # Creación del producto
        producto = Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            categoria=categoria,
            usuario=request.user  # Asignamos el usuario que lo creó
        )
        return redirect('productos_list')  # Redirigimos a la lista de productos

    # En caso de que la petición sea GET, cargamos las categorías para mostrar en el formulario
    categorias = Categoria.objects.all()
    return render(request, 'productos/crear_producto.html', {'categorias': categorias})

# Vista para editar un producto
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
        producto.save()  # Guardamos los cambios

        return redirect('productos_list')  # Redirigimos a la lista de productos

    categorias = Categoria.objects.all()
    return render(request, 'productos/editar_producto.html', {'producto': producto, 'categorias': categorias})

# Vista para eliminar un producto
@login_required
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == 'POST':
        producto.delete()  # Eliminamos el producto
        return redirect('productos_list')  # Redirigimos a la lista de productos

    return render(request, 'productos/eliminar_producto.html', {'producto': producto})

# Vista para mostrar los productos de una categoría específica
def productoPorCategoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)
    productos = categoria.productos.all()
    return render(request, 'productos/productosPorCategoria.html', {'categoria': categoria, 'productos': productos})

# Vista para listar las categorías
def categorias_list(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/categorias.html', {'categorias': categorias})

# Vista para crear una categoría
@login_required
def crear_categoria(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = Categoria.objects.create(nombre=nombre)
        return redirect('categorias_list')
    
    return render(request, 'categorias/crear_categoria.html')

# Vista para editar una categoría
@login_required
def editar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.nombre = request.POST['nombre']
        categoria.save()
        return redirect('categorias_list')
    
    return render(request, 'categorias/editar_categoria.html', {'categoria': categoria})

# Vista para eliminar una categoría
@login_required
def eliminar_categoria(request, categoria_id):
    categoria = get_object_or_404(Categoria, id=categoria_id)

    if request.method == 'POST':
        categoria.delete()
        return redirect('categorias_list')

    return render(request, 'categorias/eliminar_categoria.html', {'categoria': categoria})




