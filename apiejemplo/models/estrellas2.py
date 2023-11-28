from django.db import models
from apiejemplo.models import CustomUser
from apiejemplo.models import Desafios



class Estrellas2(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='usuariodesafio')
    desafio = models.ForeignKey(Desafios, on_delete=models.CASCADE, related_name='desafios')
    estrellas = models.IntegerField()

    def __str__(self):
        return self.usuario.username + " " + self.nivel.nombre + " " + str(self.estrellas)
