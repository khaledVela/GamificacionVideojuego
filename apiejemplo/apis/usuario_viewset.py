from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from rest_framework import viewsets, serializers, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apiejemplo.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    # permission_classes = (IsAuthenticated,)

    def list(self, request, *args, **kwargs):
        if request.user.tipo == '1':
            return super().list(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def create(self, request, *args, **kwargs):
        CustomUser.objects.create_user(username=request.data['username'],
                                        email= request.data['email'],
                                        password=request.data['password'],
                                        tipo = request.data['2'],
                                        is_active=True)
        return  HttpResponse("¡Hola, mundo!")

    def update(self, request, *args, **kwargs):
        if request.user.id == kwargs['pk'] or request.user.tipo == '1':
            if request.data.get('password'):
                _mutable = request.data._mutable
                request.data._mutable = True
                # Obtener la contraseña proporcionada por el usuario
                password = request.data.get('password')
                tipo = CustomUser.objects.get(id=kwargs['pk']).tipo
                # Encriptar la contraseña usando make_password
                hashed_password = make_password(password)
                # Actualizar la solicitud con la contraseña encriptada
                request.data['password'] = hashed_password
                request.data['tipo'] = tipo
                request.data._mutable = _mutable
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def destroy(self, request, *args, **kwargs):
        if (request.user.tipo == '1' or request.user.id == kwargs['pk']):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], url_path='buscar_usuario')
    def buscar_usuario(self, request):
        query = request.POST.get('q', '')
        usuarios = CustomUser.objects.filter(username__startswith = query)
        serializer = CustomUserSerializer(usuarios, many=True)
        return Response(serializer.data)