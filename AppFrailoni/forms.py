from django import forms

class ClienteForms(forms.Form):
    nombre= forms.CharField(label="Ingrese su nombre:", max_length=150)
    correo= forms.EmailField(label="Ingrese su correo:")
    numerocel= forms.IntegerField(label="Ingrese su número de telefono:")


class ProductoForms(forms.Form):
    nombreprod= forms.CharField(label="Ingrese el nombre del producto que le gustaria que diseñemos:", max_length=150)
    caracteristicas= forms.CharField(label="Ingrese las caracteristicas que le gustaria que tenga:", max_length=150)
    precio= forms.IntegerField(label="Ingrese su presupuesto máximo que pagaria por el producto:")

class ProveedoresForms (forms.Form):
    nombreproveedor= forms.CharField(label="Ingrese su nombre/marca:", max_length=150)
    productoproveedor= forms.CharField(label="Ingrese el producto o materia prima que nos desea vender:", max_length=150)
    precio= forms.IntegerField(label="Ingrese el precio por kilo:")