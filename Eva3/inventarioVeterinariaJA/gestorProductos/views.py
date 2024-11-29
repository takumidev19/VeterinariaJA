from django.shortcuts import render

# Create your views here.
def productos_list(request):
    return render(request, 'productos.html')

def categorias_list(request):
    return render(request, 'categorias.html')