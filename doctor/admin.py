from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Account, Doctor, Speciality, Appointment


class AccountInline(admin.StackedInline):
    model = Account


class UserAdmin(UserAdmin):
    inlines = [AccountInline]


class SpecialityAdmin(admin.ModelAdmin):
    """Model administration interface for Speciality."""
    list_display = ('speciality', 'description')


class DoctorAdmin(admin.ModelAdmin):
    filter_horizontal = ('specialities',)


admin.site.register(Appointment)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Speciality, SpecialityAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
