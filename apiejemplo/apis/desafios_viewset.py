from rest_framework import viewsets, serializers, status
from rest_framework.response import Response

from apiejemplo.apis.simple_serializers import EstrellasSerializer
from apiejemplo.models import Desafios


class DesafiosSerializer(serializers.ModelSerializer):
    estrellas = EstrellasSerializer(read_only=True)
    estrellas_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Desafios
        fields = '__all__'

class DesafiosViewset(viewsets.ModelViewSet):
    queryset = Desafios.objects.all()
    serializer_class = DesafiosSerializer

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
