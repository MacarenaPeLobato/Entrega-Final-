from django.urls import path
from AppFrailoni.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path("producto/", producto, name= "producto"),
    path("proveedores/", proveedores, name= "proveedores"),
    path("cliente/", cliente, name= "cliente"),
    path("inicio/", inicio, name= "inicio"),
    path("busquedadedatos/", busquedadedatos, name= "busquedadedatos"),
    path("busqueda/", busqueda, name= "busqueda"),
    path("leerclientes/", leerclientes, name= "leerclientes"),
    path("eliminarclientes/<id>", eliminarclientes, name= "eliminarclientes"),
    path("editarcliente/<id>", editarcliente, name= "editarcliente"),
    path("registro/", registro, name= "registro"),
    path("login/", loginusuario, name= "login"),
    path("logout/", LogoutView.as_view(), name= "logout"),
    path("editarperfil/", editarperfil, name= "editarperfil"),
    path("agregarAvatar/", agregarAvatar, name= "agregarAvatar"),
    
    


]

