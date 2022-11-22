from django.db import models

# Create your models here.
class Profesor(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.TextField(max_length=50)
    fechaCreacion = models.DateField()
    estado = models.IntegerField()

class Alumno(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.TextField(max_length=50)
    fechaCreacion = models.DateField()
    estado = models.IntegerField()

class Asignatura(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField(max_length=256)
    fechaCreacion = models.DateField()
    estado = models.IntegerField()

class Plataforma(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField(max_length=256)
    fechaCreacion = models.DateField()
    estado = models.IntegerField()

class Agenda(models.Model):
    id = models.BigAutoField(primary_key=True)
    fechaHoraInicio = models.DateField()
    fechaHoraTermino = models.DateField()
    asignatura = models.ForeignKey(Asignatura, on_delete=models.PROTECT) #? Clave Foranea
    profesor = models.ForeignKey(Profesor, on_delete=models.PROTECT) #? Clave Foranea
    estado = models.IntegerField()
    agendaAnterior = models.ForeignKey("self", on_delete=models.PROTECT) #? Clave Foranea
    link = models.TextField(max_length=256)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.PROTECT) #? Clave Foranea

class Asistencia(models.Model):
    id = models.BigAutoField(primary_key=True)
    descripcion = models.TextField(max_length=256)
    fechaCreacion = models.DateField()
    estado = models.IntegerField()
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT) #? Clave Foranea
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT) #? Clave Foranea

class FormaPago(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.TextField(max_length=256)
    fechaCreacion = models.DateField()
    estado = models.IntegerField()

class Pago(models.Model):
    id = models.BigAutoField(primary_key=True)
    agenda = models.ForeignKey(Agenda, on_delete=models.PROTECT) #? Clave Foranea
    fechaPago = models.DateField()
    formaPago = models.ForeignKey(FormaPago, on_delete=models.PROTECT) #? Clave Foranea
    alumno = models.ForeignKey(Alumno, on_delete=models.PROTECT) #? Clave Foranea
    monto = models.IntegerField()
    estado = models.IntegerField()
    comision = models.IntegerField()