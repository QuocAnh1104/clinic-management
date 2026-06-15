from django.urls import path
from . import views

app_name = 'patient_portal'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('change-password/', views.change_password, name='change_password'),
    path('dashboard/', views.my_dashboard, name='my_dashboard'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('appointments/', views.my_appointments, name='my_appointments'),
    path('appointment/<int:pk>/cancel/', views.cancel_appointment, name='cancel_appointment'),
    path('history/', views.my_history, name='my_history'),
    path('history/<int:appointment_id>/', views.history_detail, name='history_detail'),
]