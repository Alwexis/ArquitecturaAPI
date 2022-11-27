from datetime import date, datetime
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from ArquitecturaAPP.models import *
from ArquitecturaAPP.serializers import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.

#? Agendar una clase
@csrf_exempt
def agendarClase(request):
    if request.method == 'POST':
        bodyDict = request.POST.dict()
        if (bodyDict['fechaInicio'] and bodyDict['fechaTermino'] and bodyDict['asignatura'] and
        bodyDict['profesor'] and bodyDict['link'] and bodyDict['plataforma']):
            profesorInstance = get_object_or_404(Profesor, rut=bodyDict['profesor'])
            asignaturaInstance = get_object_or_404(Asignatura, id=bodyDict['asignatura'])
            plataformaInstance = get_object_or_404(Plataforma, id=bodyDict['plataforma'])
            agendaData = {
                'fechaHoraInicio': bodyDict.get('fechaInicio'),
                'fechaHoraTermino': bodyDict.get('fechaTermino'),
                'asignatura': asignaturaInstance.id,
                'profesor': profesorInstance.rut,
                'estado': 1,
                'agendaAnterior': None,
                'link': bodyDict.get('link'),
                'plataforma': plataformaInstance.id
            }
            agenda = AgendaSrlz(data=agendaData)
            if agenda.is_valid(raise_exception=True):
                agenda.save()
                return JsonResponse(agendaData, status=200)
        return JsonResponse({'error': 'Por favor ingrese todos los datos necesarios (fecha-hora inicio, fecha-hora fin, profesor, asignatura, link y plataforma).'},
                                status=400)
    return JsonResponse({'error': 'Method doesnt exist'}, status=405)

#? Valorar una clase
@csrf_exempt
def valorarClase(request):
    if request.method == 'POST':
        bodyDict = request.POST.dict()
        if (bodyDict['clase'] and bodyDict['alumno'] and bodyDict['valoracion']):
            alumnoInstance = get_object_or_404(Alumno, rut=bodyDict['alumno'])
            claseInstance = get_object_or_404(Agenda, id=bodyDict['clase'])
            asistencia = Asistencia.objects.all().filter(alumno=alumnoInstance, agenda=claseInstance)
            if asistencia:
                valoro = Valoracion.objects.all().filter(alumno=alumnoInstance, agenda=claseInstance)
                if valoro.count() == 0:
                    fecha = date.today()
                    valoracionData = {
                        'alumno': alumnoInstance.rut,
                        'agenda': claseInstance.id,
                        'nota': bodyDict.get('valoracion', 1),
                        'descripcion': bodyDict.get('descripcion'),
                        'fechaCreacion': fecha,
                        'estado': 1
                    }
                    valoracion = ValoracionSrlz(data=valoracionData)
                    if valoracion.is_valid(raise_exception=True):
                        valoracion.save()
                        return JsonResponse(valoracionData, status=201, safe=False)
                        # El estatus 201 significa que se ha creado un recurso
                    return JsonResponse({'error': 'Valoración no válida'}, status=404)
                    # El estatus 404 significa que no se ha encontrado el recurso
                return JsonResponse({'error': f'El Alumno {bodyDict["alumno"]} ya ha valorado la clase {bodyDict["clase"]}.'},
                                    status=404)
            return JsonResponse({'error': f'El Alumno {bodyDict["alumno"]} no ha asistido a la clase {bodyDict["clase"]}.'},
                                status=404)
        return JsonResponse({'error': 'Por favor ingrese todos los datos necesarios (clase, alumno y valoración).'}, status=400)
    return JsonResponse({'error': 'Method doesnt exist'}, status=405)
    # El estatus 405 significa que el método no está permitido

# Viewset
class alumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSrlz

class profesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSrlz

class asignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSrlz

class plataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSrlz

class agendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSrlz

class asistenciaViewSet(viewsets.ModelViewSet):
    queryset = Asistencia.objects.all()
    serializer_class = AsistenciaSrlz

class formaPagoViewSet(viewsets.ModelViewSet):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoSrlz

class pagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSrlz

class valoracionViewSet(viewsets.ModelViewSet):
    queryset = Valoracion.objects.all()
    serializer_class = ValoracionSrlz