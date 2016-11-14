# coding=utf-8

from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from .models import Agenda, Paciente, Medico, Consultorio

class AgendaRegistroForm(forms.Form):
    id_medico = forms.ModelChoiceField(
        queryset=Medico.objects.all().order_by('usuario_id'),
        label='Medico',
        widget=forms.Select
    )

"""
class AgendaRegistroForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ["ccedula_profesional"]
"""




