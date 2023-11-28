from django.db import models
from apiejemplo.models import CustomUser
from apiejemplo.models import Niveles



class Estrellas(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='usuarionivel')
    nivel = models.ForeignKey(Niveles, on_delete=models.CASCADE, related_name='nivel')
    estrellas = models.IntegerField()

    def __str__(self):
        return self.usuario.username + " " + self.nivel.nombre + " " + str(self.estrellas)
