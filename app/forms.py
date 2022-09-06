from django import forms

from .models import Appointment, ClassName


class AppointmentCreationForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_name'].queryset = ClassName.objects.none()

        if 'teacher' in self.data:
            try:
                teacher_id = int(self.data.get('teacher'))
                self.fields['class_name'].queryset = ClassName.objects.filter(teacher_id=teacher_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['class_name'].queryset = self.instance.teacher.classname_set.all()
# Refereces the city field in models line 22