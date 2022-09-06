from django.contrib import admin

# Register your models here.
from .models import ClassName, Teacher, Appointment

admin.site.register(ClassName)
admin.site.register(Teacher)
admin.site.register(Appointment)