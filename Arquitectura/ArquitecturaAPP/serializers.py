from rest_framework import serializers
from ArquitecturaAPP.models import *

class AlumnoSrlz(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'

class ProfesorSrlz(serializers.ModelSerializer):
    class Meta:
        model = Profesor
        fields = '__all__'

class AsignaturaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class PlataformaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class AgendaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Agenda
        fields = '__all__'

class AsistenciaSrlz(serializers.ModelSerializer):
    class Meta:
        model = Asistencia
        fields = '__all__'

class FormaPagoSrlz(serializers.ModelSerializer):
    class Meta:
        model = FormaPago
        fields = '__all__'

class PagoSrlz(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class ValoracionSrlz(serializers.ModelSerializer):
    class Meta:
        model = Valoracion
        fields = '__all__'