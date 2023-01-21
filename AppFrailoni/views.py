from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from AppFrailoni.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.

def inicio(request):
    return render (request, "inicio.html")

@login_required
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
    

@login_required   
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


@login_required
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





@login_required
def busquedadedatos(request):
    return render (request, "busquedadedatos.html")

@login_required
def busqueda(request):

    nombreprod= request.GET["nombreprod"]
    if nombreprod != "":
        productos=Producto.objects.filter(nombreprod= nombreprod)
        return render (request, "resultado.html", {"productos": productos})
        
    else:
     return render (request, "busquedadedatos.html", {"mensaje": "Datos incorrecto"})






@login_required
def leerclientes (request):
    clientes=Cliente.objects.all()     
    return render (request, "clientemod.html", {"clientes": clientes, "avatar": obtenerAvatar(request)})



@login_required
def eliminarclientes (request, id): 
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    clientes=Cliente.objects.all()
    return render (request, "cliente.html", {"clientes": clientes , "mensaje": "Usted ha seleccionado la opción  de ELIMINAR. Su elección fue ejecutada con éxito"})

@login_required
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



def registro (request): 
    if request.method=="POST":
        form= UserCreationForm (request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            form.save()
            return render ( request, "inicio.html", {"mensaje": f"El usuario: {username} ha sido creado correctamente."})
        else:
            return render (request, "registro.html", {"form": form , "mensaje": "Error al crear el usuario. Por favor, intente de nuevo"})
    else: 
        form= RegistroUsuarioform() 
        return render (request, "registro.html", {"form": form})
    


def loginusuario (request):
    if request.method=="POST":
        form= AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usu=info["username"]
            clave=info["password"]
            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render (request, "inicio.html", {"mensaje": f"El usuario: {usu} ha sido logueado correctamente."})
            else:
                return render (request, "login.html", {"form": form , "mensaje": "Error al loguearse. Usuario o contra incorrecta."})
    else: 
        form= AuthenticationForm() 
        return render (request, "login.html", {"form": form})
    
@login_required
def editarperfil(request):
    usuario=request.user
    if request.method== "POST":
        form=Perfileditado (request.POST)
        if form.is_valid():
            info= form.cleaned_data
            usuario.username= info["username"]
            usuario.email= info["email"]
            usuario.password1= info["password1"]
            usuario.password2= info["password2"]
            usuario.save()
            return render (request, "inicio.html", {"mensaje": f"Tu información ha sido modificada. Tu usuario ahora es: {usuario.username}"})
        else:
            return render (request, "editarperfil.html", {"form":form, "nombreusuario": usuario.username})
    else:
        form=Perfileditado(instance=usuario)
        return render (request,"editarperfil.html", {"form":form, "nombreusuario": usuario.username})



def obtenerAvatar(request):
    lista=Avatar.objects.filter(user=request.user)
    if len(lista)!=0:
        avatar=lista[0].imagen.url
    else:
        avatar='/media/avatarpordefecto.png'
    return avatar


def agregarAvatar(request):
    if request.method== "POST":
        form=AvatarForm (request.POST, request.FILES)
        if form.is_valid():
            avatar= Avatar(user=request.user,imagen=request.FILES["imagen"])
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)>0:
                avatarViejo[0].delete()
            avatar.save()
            return render (request, "inicio.html", {"mensaje": "El avatar agregado correctamente."})
        else:
            return render (request, "agregarAvatar.html", {"form":form, "usuario": request.user, "mensaje": "Error al cargar el avatar. Intente de nuevo"})
    else:
        form=AvatarForm
        return render (request,"agregarAvatar.html", {"form":form, "usuario": request.user})

