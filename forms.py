# coding=utf-8
from django import forms
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from medicadmin.choices import *
from .models import Especialidad, Universidad, Ubicacion


class MedicoRegistroForm(forms.Form):
    first_name = forms.CharField(
        min_length=2,
        label='Nombre',
        widget=forms.TextInput()
    )
    last_name = forms.CharField(
        min_length=2,
        label='Apellido',
        widget=forms.TextInput()
    )
    ccorreo = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput()
    )
    ccedula_especialidad = forms.CharField(
        min_length=12,
        label='Cédula profesional',
        widget=forms.TextInput()

    )
    id_universidad = forms.ModelChoiceField(
        queryset=Universidad.objects.all().order_by('cuniversidad'),
        label='Universidad',
        widget=forms.Select
    )
    id_especialidad = forms.ModelChoiceField(
        queryset=Especialidad.objects.all().order_by('cespecialidad'),
        label='Especialidad',
        widget=forms.Select
    )
    cgenero = forms.ChoiceField(
        label='Genero',
        choices=SEX_CHOICE,
        widget=forms.Select()
    )
    dtfecha_nacimiento = forms.DateField(
        label='Fecha de nacimiento',
        widget=forms.SelectDateWidget(years=range(1900, 2016))
    )
    itelefono = forms.IntegerField(
        validators=[
            MaxValueValidator(9999999999), ],
        label='Celular',
        widget=forms.NumberInput()
    )
    ifijo = forms.IntegerField(
        validators=[
            MaxValueValidator(9999999999), ],
        label='Telefono',
        widget=forms.NumberInput()
    )
    iext = forms.IntegerField(
        validators=[
            MaxValueValidator(99999), ],
        label='Extencion',
        widget=forms.NumberInput()
    )
    ccalle = forms.CharField(
        label='Calle',
        widget=forms.TextInput()
    )
    cnum_ext = forms.CharField(
        label='Exterior',
        widget=forms.TextInput()
    )
    cnum_int = forms.CharField(
        label='Interior',
        widget=forms.TextInput()
    )
    ccp = forms.CharField(
        label='Codigo postal',
        widget=forms.TextInput()
    )
    id_ubicacion = forms.ModelChoiceField(
        queryset=Ubicacion.objects.all().order_by('cdescripcion'),
        label='Ubicacion',
        widget=forms.Select
    )
    password = forms.CharField(
        label='Password',
        min_length=5,
        widget=forms.PasswordInput()
    )
    password2 = forms.CharField(
        label='Confirme password',
        min_length=5,
        widget=forms.PasswordInput()
    )
    photo = forms.ImageField(required=False)

    def clean_username(self):
        """Comprueba que no exista un username igual en la db"""
        username = self.cleaned_data['ccorreo']
        if User.objects.filter(username=username):
            raise forms.ValidationError('El correo ya esta en uso')
        return username

    def clean_ccorreo(self):
        """Comprueba que no exista un email igual en la db"""
        email = self.cleaned_data['ccorreo']
        if User.objects.filter(email=email):
            raise forms.ValidationError(
                'Ya existe un email igual registrado.'
            )
        return email

    def clean_password2(self):
        """Comprueba que el pass y el pass2 sean iguales"""
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('Los passwords no coinciden')
        return password2
