from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


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








class RegistroUsuarioform (UserCreationForm):
    email:forms.EmailField(label="Email")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar su contraseña", widget=forms.PasswordInput)

    class Meta: 
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}




class Perfileditado (UserCreationForm):
    username:forms.EmailField(label="Usuario")
    email:forms.EmailField(label="Email Usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar su contraseña", widget=forms.PasswordInput)

    class Meta: 
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")