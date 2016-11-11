# coding=utf-8

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models
from catalogos.models import Ubicacion
from medicadmin.choices import *


class Especialidad(models.Model):
    especialidad = models.AutoField(primary_key=True)
    cespecialidad = models.CharField("Especialidad", max_length=50,
                                     blank=False, null=True)
    cdescripcion = models.CharField("Descripcion", max_length=200,
                                    blank=False, null=True)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Especialidades'

    def __str__(self):
        return self.cespecialidad


class Universidad(models.Model):
    universidad = models.AutoField(primary_key=True)
    cuniversidad = models.CharField('Universidad', max_length=50,
                                    blank=False, null=True)
    cdescripcion = models.CharField('Descripcion', max_length=200, blank=False,
                                    null=True)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Universidades'

    def __str__(self):
        return self.cuniversidad


class Clinica(models.Model):
    clinica = models.AutoField(primary_key=True)
    cclinica = models.CharField('Clínica', max_length=100, blank=False,
                                null=True)
    cdescripcion = models.CharField('Descripcion', max_length=200, blank=False,
                                    null=True)
    ccalle = models.CharField('Calle', max_length=200, blank=False, null=True)
    cnum_int = models.CharField('Interior', max_length=10, blank=False,
                                null=True)
    cnum_ext = models.CharField('Exterior', max_length=10, blank=False,
                                null=True)
    ccp = models.CharField('Codigo postal', max_length=10, blank=False,
                           null=True)
    ubicacion = models.ForeignKey(Ubicacion)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Clinicas'

    def __str__(self):
        return str(self.id_clinica)


class Medico(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    ccedula_profesional = models.CharField('Cédula profesional',
                                           max_length=50, blank=False,
                                           null=True)
    ccedula_especialidad = models.CharField('Cédula especialidad',
                                            max_length=50, blank=False,
                                            null=True)
    especialidad = models.ForeignKey("Especialidad",
                                        on_delete=models.SET_NULL, null=True,
                                        blank=False)
    dtfecha_nacimiento = models.DateField('Fecha de nacimiento')
    cgenero = models.CharField('Genero', max_length=2, choices=SEX_CHOICE,
                               default=MALE)
    ccorreo = models.EmailField('Correo')
    universidad = models.ForeignKey(Universidad,
                                       on_delete=models.SET_NULL, null=True,
                                       blank=False)
    itelefono = models.BigIntegerField('Celular', validators=[
        MaxValueValidator(9999999999), ])
    ifijo = models.IntegerField('Teléfono fijo',
                                validators=[MaxValueValidator(9999999999), ])
    iext = models.IntegerField('Extencion',
                               validators=[MaxValueValidator(99999), ])
    cdatos_curriculares = models.CharField('Datos curriculares',
                                           max_length=500, blank=True,
                                           null=True)
    cespecialidades = models.CharField('Especialidades', max_length=500,
                                       blank=True, null=True)
    cfacebook = models.CharField('Facebook', max_length=100, blank=True,
                                 null=True)
    ctwiter = models.CharField('Twiter', max_length=50, blank=True, null=True)
    csitio_web = models.CharField('Sitio Web', max_length=200, blank=True,
                                  null=True)
    ccalle = models.CharField('Calle', max_length=200, blank=False, null=True)
    cnum_int = models.CharField('Interior', max_length=10, blank=False,
                                null=True)
    cnum_ext = models.CharField('Exterior', max_length=10, blank=False,
                                null=True)
    ccp = models.CharField('Codigo postal', max_length=10, blank=False,
                           null=True)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.SET_NULL, null=True,
                                       blank=False)
    photo = models.ImageField("Foto", upload_to='profiles', blank=True,
                              null=True)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Medicos'

    def __str__(self):
        return self.usuario.username


class Paciente(models.Model):
    paciente = models.AutoField(primary_key=True)
    cnombre = models.CharField('Nombre', max_length=50, blank=False, null=True)
    cpaterno = models.CharField('Apellido paterno', max_length=50, blank=False,
                                null=True)
    cmaterno = models.CharField('Apellido materno', max_length=50, blank=False,
                                null=True)
    dtfecha_nacimiento = models.DateField('Fecha de nacimiento')
    cgenero = models.CharField('Genero', max_length=2, choices=SEX_CHOICE,
                               default=MALE)
    ccorreo = models.EmailField('Correo')
    itelefono = models.BigIntegerField('Celular', validators=[
        MaxValueValidator(9999999999), ])
    ifijo = models.IntegerField('Teléfono fijo',
                                validators=[MaxValueValidator(9999999999), ])
    iext = models.IntegerField('Extencion',
                               validators=[MaxValueValidator(99999), ])
    calergias = models.CharField('Alergias', max_length=200, blank=True,
                                 null=True)
    cenfermedades_cronicas = models.CharField('Cronicas', max_length=200,
                                              blank=True, null=True)
    ccalle = models.CharField('Calle', max_length=200, blank=False, null=True)
    cnum_int = models.CharField('Interior', max_length=10, blank=False,
                                null=True)
    cnum_ext = models.CharField('Exterior', max_length=10, blank=False,
                                null=True)
    ccp = models.CharField('Codigo postal', max_length=10, blank=False,
                           null=True)
    ubicacion = models.ForeignKey(Ubicacion)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return str(self.id_paciente)


class Consultorio(models.Model):
    consultorio = models.AutoField(primary_key=True)
    clinica = models.ForeignKey(Clinica)
    cnumero_consultorio = models.CharField('Numero de consultorio',
                                           max_length=10, blank=True,
                                           null=True)
    cdescripcion = models.CharField('Referencia', max_length=200, blank=True,
                                    null=True)
    medico = models.ForeignKey(Medico)
    cubicacion = models.CharField('Direccion', max_length=200, blank=True,
                                  null=True)
    cdias_atencion = models.CharField('Dias de atención', max_length=200,
                                      blank=False, null=True)
    chorario_ini = models.CharField('Horario inicio', max_length=200,
                                    blank=False, null=True)
    chorario_fin = models.CharField('Horario fin', max_length=200,
                                    blank=False, null=True)
    iintervalo_consulta = models.IntegerField(default=1, blank=False,
                                              null=True)
    ifijo = models.IntegerField('Teléfono fijo',
                                validators=[MaxValueValidator(9999999999), ])
    iext = models.IntegerField('Extencion',
                               validators=[MaxValueValidator(99999), ])
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Consultorios'

    def __str__(self):
        return str(self.consultorio)


class Agenda(models.Model):
    agenda = models.AutoField(primary_key=True)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    dtfecha_cita = models.DateTimeField('Fecha cita', blank=False, null=True)
    dtfecha_fin_cita = models.DateTimeField('Fecha fin cita', blank=True,
                                            null=True)
    paciente = models.ForeignKey(Paciente)
    dtfecha_reprogramada = models.DateTimeField('Reprogramacion', blank=True,
                                                null=True)
    cobservaciones = models.CharField('Observaciones', max_length=200,
                                      blank=True, null=True)
    cestatus = models.CharField('Estatus', choices=STATUS_CHOICE,
                                max_length=15, blank=False, null=True)
    itelefono = models.BigIntegerField('Celular', validators=[
        MaxValueValidator(9999999999), ])
    ifijo = models.IntegerField('Teléfono fijo',
                                validators=[MaxValueValidator(9999999999), ])
    iext = models.IntegerField('Extencion',
                               validators=[MaxValueValidator(99999), ])
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Agendados'

    def __str__(self):
        return str(self.agenda)


class Consulta(models.Model):
    consulta = models.AutoField(primary_key=True)
    consultorio = models.ForeignKey(Consultorio, on_delete=models.CASCADE)
    dtfecha_consulta = models.DateTimeField('Fecha consulta')
    dtfecha_fin_consulta = models.DateTimeField('Fecha fin consulta')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    cestatus = models.CharField('Estatus', choices=STATUS_CHOICE,
                                max_length=10, blank=True, null=True)
    dHonorarios = models.DecimalField("honorarios", decimal_places=2,
                                      blank=False, null=True, default=0.0,
                                      max_digits=6)
    cObservaciones = models.CharField('Observaciones', max_length=200,
                                      blank=True, null=True)
    cSintomatologia = models.CharField('Sintomatología', max_length=1000,
                                       blank=False, null=True)
    cDiagnostico = models.CharField('Diagnostico', max_length=1000,
                                    blank=False, null=True)
    cita = models.OneToOneField(Agenda, null=True, blank=True)
    dtalla = models.DecimalField('Talla', blank=True, null=True,
                                 decimal_places=2, max_digits=3)
    dpeso = models.DecimalField('Peso', decimal_places=2, blank=True,
                                null=True, max_digits=3)
    iedad = models.IntegerField('Edad', blank=False, null=True)
    imeses = models.IntegerField('Meses', blank=False, null=True)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Consultas'

    def __str__(self):
        return str(self.consulta)


class Receta(models.Model):
    receta = models.AutoField(primary_key=True)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    iorden_medicamento = models.IntegerField('Orden')
    cmedicamento = models.CharField('Medicamento', max_length=200, blank=False,
                                    null=True)
    cfrecuencia = models.CharField('Frecuencia de toma', max_length=200,
                                   blank=False, null=True)
    cperiodo = models.CharField('Periodo de toma', max_length=200, blank=False,
                                null=True)
    cindicaciones = models.CharField('Indicaciones', max_length=200,
                                     blank=True, null=True)
    dtcreacion = models.DateTimeField('Creación', auto_now=True)
    activo = models.BooleanField(default=True)

    class Meta(object):
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return str(self.receta)
