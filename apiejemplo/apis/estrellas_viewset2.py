from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from apiejemplo.apis import CustomUserSerializer, DesafiosSerializer
from apiejemplo.apis.funciones import DefinEstrella
from apiejemplo.models import *


class EstrellasSerializer2(serializers.ModelSerializer):
    usuario = CustomUserSerializer(read_only=True)
    usuario_id = serializers.IntegerField(write_only=True)
    desafio = DesafiosSerializer(read_only=True)
    desafio_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Estrellas2
        fields = '__all__'


class EstrellasViewSet2(viewsets.ModelViewSet):
    queryset = Estrellas2.objects.all()
    serializer_class = EstrellasSerializer2

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
