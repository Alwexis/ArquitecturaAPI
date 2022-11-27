from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from ArquitecturaAPP.views import *

router = routers.DefaultRouter()
nombres = ['alumno', 'profesor', 'asignatura', 'plataforma', 'agenda', 'asistencia', 'formaPago', 'pago', 'valoracion']
viewSet = [alumnoViewSet, profesorViewSet, asignaturaViewSet, plataformaViewSet, agendaViewSet, asistenciaViewSet, formaPagoViewSet, pagoViewSet, valoracionViewSet]
for x in range(0, len(nombres), 1):
    router.register(nombres[x], viewSet[x])

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/valorarClase/', valorarClase, name='valorarClase'),
    path('api/agendarClase/', agendarClase, name='agendarClase'),
]
