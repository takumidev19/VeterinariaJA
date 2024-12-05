from django.db import models
from django.contrib.auth.models import User
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre