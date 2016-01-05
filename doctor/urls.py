from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', 'doctor.views.index', name='index'),
    url(r'^admin/', ' ', name='admin_page'),
    url(r'^doctor/$', 'doctor.views.doctor', name='doctor_page'),
    url(r'^patient/$', 'doctor.views.patient', name='patient_page'),
    url(r'^appointment/(?P<pk>[0-9]+)/approve/$', views.appointment_approve, name='appointment_approve'),
    url(r'^appointment/(?P<pk>[0-9]+)/reject/$', views.appointment_reject, name='appointment_reject'),
    url(r'^feedback/(?P<pk>[0-9]+)/approve/$', views.feedback_approve, name='feedback_approve'),
    url(r'^feedback/(?P<pk>[0-9]+)/reject/$', views.feedback_reject, name='feedback_reject'),
    url(r'^feedback/(?P<pk>[0-9]+)/$', views.feedback_page, name='feedback_page'),
]
