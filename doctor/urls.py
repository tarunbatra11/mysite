from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', 'doctor.views.index', name='index'),
    url(r'^doctor/$', 'doctor.views.doctor', name='doctor_page'),
    url(r'^patient/$', 'doctor.views.patient', name='patient_page'),
]
