from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    tipo = models.IntegerField(null=True, blank=True)
    last_level = models.IntegerField(null=True, blank=True)
    vidaslvl = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.username
