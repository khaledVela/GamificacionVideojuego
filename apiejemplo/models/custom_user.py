from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    tipo = models.IntegerField()
    last_level = models.IntegerField()
    vidaslvl = models.IntegerField()
    def __str__(self):
        return self.username
