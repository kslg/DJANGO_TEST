from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.appointment_create_view, name='person_add'),
    path('<int:pk>/', views.appointment_update_view, name='person_change'),


    path('ajax/load-classes/', views.load_classes, name='ajax_load_classes'), # AJAX
]