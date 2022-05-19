from distutils.command.upload import upload
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre

class Foto(models.Model):
    id = models.AutoField(primary_key=True)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    imagen = models.ImageField(null=True)

    def __str__(self) -> str:
        return f"Foto{self.id} ({self.categoria})"