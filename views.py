# coding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import MedicoRegistroForm, MedicoExtrasForm
from .models import Medico


@login_required
def dashboard_view(request):
    if request.method =='POST':
        form = MedicoExtrasForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            cdatos_curriculares = clean_data.get('cdatos_curriculares')
            cfacebook = clean_data.get('cfacebook')
            ctwiter = clean_data.get('ctwiter')
            csitio_web = clean_data.get('csitio_web')
            Medico.objects.filter(ccorreo=request.user.get_username()).update(
                cdatos_curriculares=cdatos_curriculares,
                cfacebook=cfacebook,
                ctwiter=ctwiter,
                csitio_web=csitio_web
            )
            messages.success(request, 'Datos actualizados con exito')
            return redirect(reverse('medicadmin.medico_dashboard'))
    else:
        data = {}
        form = None
        medico = Medico.objects.get(usuario=request.user)
        if medico.cdatos_curriculares is not None:
            data['cdatos_curriculares'] = medico.cdatos_curriculares
        if medico.cfacebook is not None:
            data['cfacebook'] = medico.cfacebook
        if medico.ctwiter is not None:
            data['ctwiter'] = medico.ctwiter
        if medico.csitio_web is not None:
            data['csitio_web'] = medico.csitio_web
        if data is not None:
            form = MedicoExtrasForm(initial=data)
    return render(request, 'medicadmin/medico_dashboard.html', {'form':form})


def login_view(request):
    """validar acceso de usuarios"""
    if request.user.is_authenticated():
        return redirect(reverse('medicadmin.medico_dashboard'))

    mensaje = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect(reverse('medicadmin.medico_dashboard'))
            else:
                # direccionar informando que la cuenta esta inactiva
                mensaje = 'La cuenta se encuentra inactiva'
                return render(request, 'medicadmin/login.html',
                              {'mensaje': mensaje})
        mensaje = 'Nombre de usuario o contraseña no valido'
    return render(request, 'medicadmin/login.html', {'mensaje': mensaje})


def logout_view(request):
    """Desconecta de la aplicación"""
    logout(request)
    messages.success(request, 'Te has desconectado.')
    return redirect(reverse('medicadmin.login'))


def medico_registro_view(request):
    """Registro de medicos"""
    if request.method == 'POST':
        # Si el metodo es post, obtenemos datos del formulario
        form = MedicoRegistroForm(request.POST, request.FILES)
        # Comprobamos si el formulario es vacio
        if form.is_valid():
            # En caso de ser valido, obtenemos los datos del formulario
            # form.cleaned_data obtiene los datos limpios y los pone en un
            # diccionario con pares clave/valor,
            # donde clave es el nombre del campo
            # del formulario y el valor es el valor si existe.
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('ccorreo')
            first_name = cleaned_data.get('first_name')
            last_name = cleaned_data.get('last_name')
            password = cleaned_data.get('password')
            ccorreo = cleaned_data.get('ccorreo')
            ccedula_especialidad = cleaned_data.get('ccedula_especialidad')
            ccedula_profesional = cleaned_data.get('ccedula_profesional')
            universidad = cleaned_data.get('universidad')
            especialidad = cleaned_data.get('especialidad')
            cgenero = cleaned_data.get('cgenero')
            dtfecha_nacimiento = cleaned_data.get('dtfecha_nacimiento')
            itelefono = cleaned_data.get('itelefono')
            ifijo = cleaned_data.get('ifijo')
            iext = cleaned_data.get('iext')
            ccalle = cleaned_data.get('ccalle')
            cnum_ext = cleaned_data.get('cnum_ext')
            cnum_int = cleaned_data.get('cnum_int')
            ccp = cleaned_data.get('ccp')
            ubicacion = cleaned_data.get('ubicacion')
            photo = cleaned_data.get('photo')
            # instanciamos un objeto User, con el username y password
            user_model = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
            )
            # agregamos email
            user_model.email = ccorreo
            # Y guardamos el objeto, esto guardara los datos en la db.
            user_model.save()
            # Ahora, creamos un objeto Medico, aunque no haya incluido
            # una imagen, ya quedara la referencia creada en la db.
            medico = Medico()
            # Al campo usuario le asignamos el objeto user_model
            medico.usuario = user_model
            medico.ccorreo = ccorreo
            medico.ccedula_especialidad = ccedula_especialidad
            medico.ccedula_profesional = ccedula_profesional
            medico.universidad = universidad
            medico.especialidad = especialidad
            medico.cgenero = cgenero
            medico.dtfecha_nacimiento = dtfecha_nacimiento
            medico.itelefono = itelefono
            medico.ifijo = ifijo
            medico.iext = iext
            medico.ccalle = ccalle
            medico.cnum_ext = cnum_ext
            medico.cnum_int = cnum_int
            medico.ccp = ccp
            medico.ubicacion = ubicacion
            medico.photo = photo
            # Guardamos en db
            medico.save()
            return redirect(reverse('medicadmin.gracias',
                                    kwargs={'username': username}))
    else:
        # si el método es GET, instanciamos un objeto RegistroMedicoForm vacio
        form = MedicoRegistroForm()
    # Creamos el context
    context = {
        'form': form
    }
    # y mostramos los datos en el template
    return render(request, 'medicadmin/medico_registro.html', context)


def gracias_view(request, username):
    # Pantalla de agradecimiento por el registro
    return render(request, 'medicadmin/medico_gracias.html',
                  {'username': username})
