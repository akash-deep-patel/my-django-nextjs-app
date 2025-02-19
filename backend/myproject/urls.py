from django.urls import path, include
from django.contrib import admin
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.home, name='home'),
    path('appointments/', views.schedule_appointment, name='schedule_appointment'),
    path('doctors/', views.get_doctors, name='get_doctors'),
    path('patients/', views.get_patients, name='list_patients'),
    path('login/', views.login_view, name='login'),
    path('patient_login/', views.patient_login, name='patient_login'), 
    path('doctor_login/', views.doctor_login, name='doctor_login'),  
    path('register_patient/', views.register_patient, name='register_patient'),  # Add this line
    path('register_doctor/', views.register_doctor, name='register_doctor'),
]