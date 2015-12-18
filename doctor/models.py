from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.user.username


class Speciality(models.Model):
    speciality = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.speciality


class Doctor(models.Model):
    name = models.OneToOneField(Account)
    specialities = models.ManyToManyField(Speciality)

    def __str__(self):
        return str(self.name)


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='doctor_dropdown')
    patient = models.ForeignKey(Account)
    appointment_message = models.CharField(max_length=500)
    appointment_time = models.DateTimeField(
            blank=True, null=True)
    approved_status = models.CharField(max_length=8, default='pending', editable=True)
    request_date = models.DateTimeField(
            blank=True, null=True)

    def approve(self):
        self.approved_status = 'approved'
        self.save() 

    def reject(self):
        self.approved_status = 'reject'
        self.save() 

    def __str__(self):
        return str(self.appointment_message)


class Feedback(models.Model):
    doctor = models.ForeignKey(Doctor)
    patient = models.ForeignKey(Account)
    feedback_given = models.CharField(max_length=500)
    feedback_time = models.DateTimeField(
            blank=True, null=True)
    approved_status = models.CharField(max_length=8, default='pending', editable=True)

    def approve(self):
        self.approved_status = 'approved'
        self.save() 

    def reject(self):
        self.approved_status = 'reject'
        self.save() 

    def __str__(self):
        return str(self.feedback_given)
