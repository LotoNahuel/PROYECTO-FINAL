from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class DiseñoForm(forms.Form):
    titulo = forms.CharField(max_length=100)
    diseño = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=500)
    fechaPost = forms.DateField()
    emailUsuario = forms.EmailField(max_length=50)

class RegistroForm(UserCreationForm):
    email=forms.EmailField(label="Email usuario")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}#para cada uno de los campos del formulario, le asigna un valor vacio