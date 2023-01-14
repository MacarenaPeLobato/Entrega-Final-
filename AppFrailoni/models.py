from django.db import models

# Create your models here.
class Producto (models.Model):
    nombreprod=models.CharField(max_length=200)
    caracteristicas=models.CharField(max_length=300)
    precio=models.IntegerField()
    
    def __str__(self):
        return self.nombreprod + " " + self.caracteristicas + " " + str(self.precio)


class Cliente (models.Model):
    nombre=models.CharField(max_length=50)
    numerocel=models.IntegerField()
    correo=models.EmailField()

    def __str__(self):
        return self.nombre + " " + str(self.numerocel) + " " + self.correo


class Proveedores(models.Model):
    nombreproveedor=models.CharField(max_length=150)
    productoproveedor=models.CharField(max_length=150)
    precio=models.IntegerField()

    def __str__(self):
        return self.nombreproveedor + " " + self.productoproveedor + " " + str(self.precio)

        




