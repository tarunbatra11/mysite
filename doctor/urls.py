from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', 'doctor.views.index', name='index'),
    url(r'^doctor/$', 'doctor.views.doctor', name='doctor_page'),
    url(r'^patient/$', 'doctor.views.patient', name='patient_page'),
    url(r'^appointment/(?P<pk>[0-9]+)/approve/$', views.appointment_approve, name='appointment_approve'),
    url(r'^appointment/(?P<pk>[0-9]+)/reject/$', views.appointment_reject, name='appointment_reject'),
]
