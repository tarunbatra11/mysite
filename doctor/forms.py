from django import forms
from doctor.models import Appointment, Feedback

class AppointmentForm(forms.ModelForm):
    appointment_time = forms.DateTimeField(input_formats=['%Y-%m-%d %H:%M:%S'])

    class Meta:
        model = Appointment
        fields = ('doctor', 'appointment_message', 'appointment_time')


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('feedback_given',)
