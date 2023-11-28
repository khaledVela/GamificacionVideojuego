from django.db import models

class Planetas(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=350)
    radio = models.CharField(max_length=50)
    geografia = models.CharField(max_length=250)
    temperatura = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
