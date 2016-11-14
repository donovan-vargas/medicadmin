# coding=utf-8

from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.shortcuts import render

from .form_cita import AgendaRegistroForm
from .models import Consultorio

def agenda_registro_view(request):
    if request.method == 'POST':
        form = AgendaRegistroForm(request.POST)
        if form.is_valid():
            imedico = form.cleaned_data.get('id_medico')
            queryset = Consultorio.objects.filter(medico=imedico)
            for obj in queryset:
                print ("consultorio %s " % (obj.cnumero_consultorio))
            context = {
                'query': queryset
            }
    else:
        form = AgendaRegistroForm()
        context = {
            'form': form
        }

    return render(request, 'medicadmin/agenda_registro.html', context)



