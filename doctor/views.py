from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from doctor.models import Doctor, Appointment, Account, Feedback
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
    feedbacks_received = Feedback.objects.filter(doctor=doctor_object)
    return render(request, 'doctor.html', {'new_requests' : new_requests, 'approved_appointments': approved_appointments, 'feedbacks_received': feedbacks_received})


@login_required
def patient(request):
    user = str(request.user)
    user_object = User.objects.get(username = user)
    account_object = Account.objects.get(user = user_object)
    appointment_history = Appointment.objects.filter(patient=account_object)
    approved_appointments = Appointment.objects.filter(patient=account_object, approved_status='approved')
    fo = str(timezone.now())[:19]
    pending_appointments = Appointment.objects.filter(patient=account_object, approved_status='pending', appointment_time__gte=fo)
    feedbacks_given = Feedback.objects.filter(patient=account_object)
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
    return render(request, 'patient.html', {'form': form, 'appointment_history': appointment_history, 'approved_appointments': approved_appointments,  'pending_appointments': pending_appointments, 'feedbacks_given': feedbacks_given})


@login_required
def appointment_approve(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    appointment.approve()
    return redirect('doctor.views.doctor')


@login_required
def appointment_reject(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    #post_pk = comment.post.pk
    appointment.reject()
    return redirect('doctor.views.doctor')
