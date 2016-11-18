# coding=utf-8
from django.conf.urls import url

from medicadmin.views import medico_registro_view, gracias_view, login_view, dashboard_view, logout_view
from medicadmin.view_cita import agenda_registro_view

urlpatterns = [
    url(r'^dashboard_view/$', dashboard_view, name='medicadmin.medico_dashboard'),
    url(r'^medico_registro/$', medico_registro_view,
        name='medicadmin.medico_registro'),
    url(r'^login/$', login_view, name='medicadmin.login'),
    url(r'^logout/$', logout_view, name='medicadmin.logout'),
    url(r'agenda_registro/$', agenda_registro_view,
        name='medicadmin.agenda_registro'),
    url(r'gracias/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$',
        gracias_view, name='medicadmin.gracias'),
]
