from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from apiejemplo.apis import PlanetasSerializer
from apiejemplo.models import *


class nivelesSerializer(serializers.ModelSerializer):
    planeta = PlanetasSerializer(read_only=True)
    planeta_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Niveles
        fields = '__all__'

class nivelesViewset(viewsets.ModelViewSet):
    queryset = Niveles.objects.all()
    serializer_class = nivelesSerializer

    def create(self, request, *args, **kwargs):
        if (request.user.tipo == '1'):
            return super().create(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def update(self, request, *args, **kwargs):
        if (request.user.tipo == '1'):
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if (request.user.tipo == '1'):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)