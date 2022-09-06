from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AppointmentCreationForm
from .models import Appointment, ClassName


def appointment_create_view(request):
    form = AppointmentCreationForm()
    if request.method == 'POST':
        form = AppointmentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person_add')
    return render(request, 'persons/home.html', {'form': form})


def appointment_update_view(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    form = AppointmentCreationForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentCreationForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'persons/home.html', {'form': form})


# AJAX
def load_classes(request):
    teacher_id = request.GET.get('teacher_id')
    classes = ClassName.objects.filter(teacher_id=teacher_id)
    return render(request, 'persons/city_dropdown_list_options.html', {'classes': classes})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)