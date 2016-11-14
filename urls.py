# coding=utf-8
from django.conf.urls import url

from medicadmin.views import medico_registro_view, gracias_view
from medicadmin.view_cita import agenda_registro_view

urlpatterns = [
    url(r'medico_registro/$', medico_registro_view,
        name='medicadmin.medico_registro'),
    url(r'agenda_registro/$', agenda_registro_view,
        name='medicadmin.agenda_registro'),
    url(r'gracias/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        gracias_view, name='medicadmin.gracias'),
]
