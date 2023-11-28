from django.db import models
from apiejemplo.models import Planetas


class Niveles(models.Model):

    nombre = models.CharField(max_length=50)
    planeta = models.ForeignKey(Planetas, on_delete=models.CASCADE, related_name='planeta')
    estrellas = models.IntegerField()
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre
