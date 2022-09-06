from django.db import models
from django.contrib.auth.models import User, Group
from cloudinary.models import CloudinaryField

class Teacher(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class ClassName(models.Model):
    teacher = models.ForeignKey(Teacher(), on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    name = models.CharField(max_length=124)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, blank=False, null=True)
    class_name = models.ForeignKey(ClassName, on_delete=models.SET_NULL, blank=False, null=True)

    def __str__(self):
        return self.name