from django.urls import path, include
from rest_framework import routers

from apiejemplo.apis import *

router = routers.DefaultRouter()

router.register(r'planetas', planetas_viewset.PlanetasViewset)
router.register(r'niveles', niveles_viewset.nivelesViewset)
router.register(r'desafios', desafios_viewset.DesafiosViewset)
router.register(r'estrellas', estrellas_viewset.EstrellasViewSet)
router.register(r'usuarios', usuario_viewset.CustomUserViewSet)
router.register(r'estrellas2', estrellas_viewset2.EstrellasViewSet2)


urlpatterns = [
    path('', include(router.urls)),
]
