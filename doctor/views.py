from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from doctor.models import Doctor, Appointment, Account
from doctor.forms import AppointmentForm
import logging
from django.http import HttpResponseRedirect
from django.utils import timezone

logger = logging.getLogger(__name__)

@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def doctor(request):

    user = str(request.user)
    user_object = User.objects.get(username = user)
    account_object = Account.objects.get(user = user_object)
    doctor_object = Doctor.objects.get(name = account_object)
    fo = str(timezone.now())[:19]
    new_requests = Appointment.objects.filter(doctor=doctor_object, approved_status='pending', appointment_time__gte=fo)
    approved_appointments = Appointment.objects.filter(doctor=doctor_object, approved_status='approved', appointment_time__gte=fo)
    return render(request, 'doctor.html', {'new_requests' : new_requests, 'approved_appointments': approved_appointments})


@login_required
def patient(request):

    # get appointment history
    user = str(request.user)
    user_object = User.objects.get(username = user)
    account_object = Account.objects.get(user = user_object)
    appointment_history = Appointment.objects.filter(patient=account_object)
    approved_appointments = Appointment.objects.filter(patient=account_object, approved_status='approved')
    fo = str(timezone.now())[:19]
    pending_appointments = Appointment.objects.filter(patient=account_object, approved_status='pending', appointment_time__gte=fo)
    if request.method == "POST":
       form = AppointmentForm(request.POST)
       if form.is_valid():
           post = form.save(commit=False)
           post.patient = account_object
           post.request_date = timezone.now()
           post.save()
           return HttpResponseRedirect('/')
    else:
        form = AppointmentForm()
    return render(request, 'patient.html', {'form': form, 'appointment_history': appointment_history, 'approved_appointments': approved_appointments,  'pending_appointments': pending_appointments})
