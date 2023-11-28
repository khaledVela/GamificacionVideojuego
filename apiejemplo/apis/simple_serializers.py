from rest_framework import serializers

from apiejemplo.models import *


class PlanetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planetas
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class DesafiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desafios
        fields = '__all__'

class NivelesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Niveles
        fields = '__all__'

class EstrellasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estrellas
        fields = '__all__'