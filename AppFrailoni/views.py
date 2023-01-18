from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppFrailoni.forms import *


# Create your views here.

def inicio(request):
    return render (request, "inicio.html")


def producto(request):
    if request.method== "POST":
        form=ProductoForms (request.POST)
        if form.is_valid():
            infoprod= form.cleaned_data
            nombreprod= infoprod["nombreprod"]
            caracteristicas= infoprod["caracteristicas"]
            precio= infoprod["precio"]
            formuprod=Producto( nombreprod=nombreprod, caracteristicas=caracteristicas, precio=precio)
            formuprod.save()        
            return render (request, "inicio.html", {"mensaje": "Tu información sobre el producto ha sido enviada. A la brevedad nos comunicaremos y la tendremos en cuenta para diseñar tu producto."})
        else :
            return render (request, "producto.html", {"form": form, "mensaje": "Información no valida. Completo erroneamente el fomulario de PRODUCTO"})
    else:
        infoprod1= ProductoForms()
        return render (request, "producto.html", {"form": infoprod1 })
    
    
def proveedores(request):
    if request.method== "POST":
        form=ProveedoresForms (request.POST)
        if form.is_valid():
            info4= form.cleaned_data
            nombreproveedor= info4["nombreproveedor"]
            productoproveedor= info4["productoproveedor"]
            precio= info4["precio"]
            formuproveedor= Proveedores( nombreproveedor=nombreproveedor, productoproveedor=productoproveedor, precio=precio)
            formuproveedor.save()        
            return render (request, "inicio.html", {"mensaje": "Tu información ha sido enviada. A la brevedad, nos contactaremos. ¡¡Muchas gracias!!"})
        else :
            return render (request, "proveedores.html", {"form": form, "mensaje": "Información no valida. Completo erroneamente el fomulario de PROVEEDORES"})
    else:
        info3= ProveedoresForms()
        return render (request, "proveedores.html", {"form": info3 })

    
def cliente(request):
    if request.method== "POST":
        form=ClienteForms (request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            correo= info["correo"]
            numerocel= info["numerocel"]
            formucliente=Cliente( nombre=nombre, correo=correo, numerocel=numerocel)
            formucliente.save()        
            return render (request, "inicio.html", {"mensaje": "Tu información ha sido enviada. A la brevedad, nos contactaremos."})
        else :
            return render (request, "cliente.html", {"form": form, "mensaje": "Información no valida. Completo erroneamente el fomulario de CLIENTES"})
    else:
        info1= ClienteForms()
        return render (request, "cliente.html", {"form": info1 })






def busquedadedatos(request):
    return render (request, "busquedadedatos.html")


def busqueda(request):

    nombreprod= request.GET["nombreprod"]
    if nombreprod != "":
        productos=Producto.objects.filter(nombreprod= nombreprod)
        return render (request, "resultado.html", {"productos": productos})
        
    else:
     return render (request, "busquedadedatos.html", {"mensaje": "Datos incorrecto"})







def leerclientes (request):
    clientes=Cliente.objects.all()
    return render (request, "clientemod.html", {"clientes": clientes})

def eliminarclientes (request, id): 
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    clientes=Cliente.objects.all()
    return render (request, "cliente.html", {"clientes": clientes , "mensaje": "Usted ha seleccionado la opción  de ELIMINAR. Su elección fue ejecutada con éxito"})


def editarcliente(request, id):
    cliente=Cliente.objects.get(id=id)
    if request.method== "POST":
        form=ClienteForms (request.POST)
        if form.is_valid():
            info= form.cleaned_data
            cliente.nombre= info["nombre"]
            cliente.correo= info["correo"]
            cliente.numerocel= info["numerocel"]
            cliente.save()
            clientes=Cliente.objects.all()        
            return render (request, "cliente.html", {"clientes": clientes , "mensaje": "Tu información ha sido modificada."})
        pass
    else:
        formulario= ClienteForms(initial={"nombre": cliente.nombre , "correo": cliente.correo , "numerocel":cliente.numerocel})
        return render ( request, "editarcliente.html", {"form": formulario, "cliente": cliente })

