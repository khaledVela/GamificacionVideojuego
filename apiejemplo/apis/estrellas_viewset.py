from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from apiejemplo.apis import CustomUserSerializer, NivelesSerializer, DefinEstrella
from apiejemplo.models import *


class EstrellasSerializer(serializers.ModelSerializer):
    usuario = CustomUserSerializer(read_only=True)
    usuario_id = serializers.IntegerField(write_only=True)
    nivel = NivelesSerializer(read_only=True)
    nivel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Estrellas
        fields = '__all__'


class EstrellasViewSet(viewsets.ModelViewSet):
    queryset = Estrellas.objects.all()
    serializer_class = EstrellasSerializer

    def create(self, request, *args, **kwargs):
        request.data['estrellas'] = DefinEstrella(request)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
