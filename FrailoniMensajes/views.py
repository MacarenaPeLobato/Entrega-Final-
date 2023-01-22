from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from FrailoniMensajes.forms import *




# Create your views here.

def inicio(request):
    return render (request, "inicio.html")


def chat (request):
    if request.method== "POST":
        chatcito= chatForm(request.POST)
        if chatcito.is_valid():
            informacion= chatcito.cleaned_data
            chat1= Chat(mensaje=informacion["mensaje"])
            chat1.save()        
            return render (request, "inicio.html", {"mensaje": "Tu mensaje ha sido enviado."})
    else:
        chatcito=chatForm()
    return render (request, "chatenviar.html", {"chatcito": chatcito})

   