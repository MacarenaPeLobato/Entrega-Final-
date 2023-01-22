from django.urls import path
from FrailoniMensajes.views import *




urlpatterns = [
    path("chat/", chat, name= "chat"),
    path("inicio/", inicio, name= "inicio"),     

]