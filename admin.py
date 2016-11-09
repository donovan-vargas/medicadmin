from django.contrib import admin
from .models import Especialidad, Universidad, Clinica, Medico, Paciente, \
    Consultorio, Agenda, Consulta, Receta


# Register your models here.
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = (
        'especialidad', 'cespecialidad', 'cdescripcion', 'dtcreacion',
        'activo',)
    search_fields = ('cespecialidad', 'cdescripcion',)
    list_filter = ('dtcreacion',)


class UniversidadAdmin(admin.ModelAdmin):
    list_display = (
        'universidad', 'cuniversidad', 'cdescripcion', 'dtcreacion',
        'activo',)
    search_fields = ('cuniversidad', 'cdescripcion',)
    list_filter = ('dtcreacion',)


class ClinicaAdmin(admin.ModelAdmin):
    list_display = (
        'clinica', 'cclinica', 'cdescripcion', 'ccalle', 'cnum_int',
        'cnum_ext', 'ccp', 'ubicacion', 'dtcreacion',
        'activo',)
    search_fields = ('cclinica', 'cdescripcion',)
    list_filter = ('dtcreacion',)


class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'usuario', 'ccedula_profesional', 'ccedula_especialidad',
        'especialidad', 'dtfecha_nacimiento', 'cgenero',
        'ccorreo', 'universidad', 'itelefono', 'ifijo',
        'iext', 'cdatos_curriculares', 'cespecialidades',
        'cfacebook', 'ctwiter', 'csitio_web', 'ccalle', 'cnum_int', 'cnum_ext',
        'ccp', 'ubicacion', 'dtcreacion',
        'activo',)
    search_fields = (
        'usuario', 'ccedula_profesional', 'ccedula_especialidad',
        'dtfecha_nacimiento', 'ccorreo', 'ccalle', 'cnum_int',
        'cnum_ext', 'ccp',)
    list_filter = ('dtfecha_nacimiento', 'dtcreacion',)


class PacienteAdmin(admin.ModelAdmin):
    list_display = (
        'paciente', 'cnombre', 'cpaterno', 'cmaterno', 'dtfecha_nacimiento',
        'cgenero', 'ccorreo', 'itelefono', 'ifijo',
        'iext', 'calergias', 'cenfermedades_cronicas', 'ccalle', 'cnum_int',
        'cnum_ext', 'ccp', 'ubicacion',
        'dtcreacion', 'activo',)
    search_fields = (
        'cnombre', 'cpaterno', 'cmaterno', 'dtfecha_nacimiento', 'calergias',
        'cenfermedades_cronicas',)
    list_filter = ('dtfecha_nacimiento', 'dtcreacion',)


class ConsultorioAdmin(admin.ModelAdmin):
    list_display = (
        'consultorio', 'clinica', 'cnumero_consultorio', 'cdescripcion',
        'medico', 'cubicacion', 'cdias_atencion',
        'chorario_ini', 'chorario_fin', 'iintervalo_consulta', 'dtcreacion',
        'activo',)
    search_fields = (
        'clinica', 'cnumero_consultorio', 'cdescipcion', 'idmedico',)
    list_filter = ('dtcreacion',)


class AgendaAdmin(admin.ModelAdmin):
    list_display = (
        'agenda', 'consultorio', 'dtfecha_cita', 'dtfecha_fin_cita',
        'paciente', 'dtfecha_reprogramada',
        'cobservaciones', 'cestatus', 'itelefono', 'ifijo', 'iext',
        'dtcreacion', 'activo',)
    search_fields = (
        'consultorio', 'dtfecha_cita', 'paciente',
        'dtfecha_reprogramada', 'cobsevaciones', 'cestatus',)
    list_filter = ('dtfecha_cita', 'dtfecha_fin_cita', 'dtfecha_reprogramada',)


class ConsultaAdmin(admin.ModelAdmin):
    list_display = (
        'consulta', 'consultorio', 'dtfecha_consulta',
        'dtfecha_fin_consulta', 'paciente', 'medico', 'cestatus',
        'dHonorarios', 'cObservaciones', 'cSintomatologia', 'cDiagnostico',
        'cita', 'dtalla', 'dpeso', 'iedad', 'imeses',
        'dtcreacion', 'activo',)
    search_fields = (
        'consulta', 'consultorio', 'dtfecha_consulta',
        'dtfecha_fin_consulta', 'paciente', 'medico',
        'cestatus',)
    list_filter = (
        'dtfecha_consulta', 'dtfecha_fin_consulta', 'dtcreacion', 'dpeso',
        'dtalla',)


class RecetaAdmin(admin.ModelAdmin):  # constulta
    list_display = (
        'receta', 'consulta', 'iorden_medicamento', 'cmedicamento',
        'cfrecuencia', 'cperiodo', 'cindicaciones',
        'dtcreacion', 'activo',)
    search_fields = (
        'receta', 'consulta', 'iorden_medicamento', 'cmedicamento',)
    list_filter = ('dtcreacion',)


admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Universidad, UniversidadAdmin)
admin.site.register(Clinica, ClinicaAdmin)
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Consultorio, ConsultorioAdmin)
admin.site.register(Agenda, AgendaAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Receta, RecetaAdmin)
