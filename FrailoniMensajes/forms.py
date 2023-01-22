from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class chatForm(forms.Form):
    mensaje= forms.CharField(label="Ingrese su mensaje:", max_length=500)
    