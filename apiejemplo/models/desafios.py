from django.db import models


class Desafios(models.Model):

    nombre = models.CharField(max_length=50)
    estrellas = models.IntegerField()
    descripcion = models.CharField(max_length=250)


    def __str__(self):
        return self.nombre
