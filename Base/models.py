from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Diseño(models.Model):
    titulo = models.CharField(max_length=100)
    diseño = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=500)
    fechaPost = models.DateField()
    emailUsuario = models.EmailField(max_length=50)
    
class Comentario(models.Model):
    comentario = models.CharField(max_length=150)
    fechaComentario = models.DateField()