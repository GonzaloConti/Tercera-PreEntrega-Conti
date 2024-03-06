from django.db import models

# Create your models here.

class Empleado(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    puesto = models.CharField(max_length=50)
    
    
    def __str__(self):

        return f"{self.nombre} --- {self.apellido} --- {self.puesto}"
    

class Vacante(models.Model):
    
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    requisitos = models.CharField(max_length=300)
    salario = models.IntegerField()
    
    def __str__(self):

        return f"{self.titulo} --- {self.salario}"


class Departamento(models.Model):
    
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    

    def __str__(self):

        return f"{self.nombre}"