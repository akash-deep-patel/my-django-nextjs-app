
from django.http import JsonResponse
from .models import Doctor, Patient, Appointment
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests

def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if user_type == 'patient':
            try:
                patient = Patient.objects.get(email=username)
                if patient.password == password:
                    # Redirect to patient login page with available doctors
                    doctors = Doctor.objects.all()
                    return render(request, 'patient_login.html', {'doctors': doctors, 'patient': patient})
                else:
                    return render(request, 'login.html', {'error': 'Invalid credentials'})
            except Patient.DoesNotExist:
                return render(request, 'login.html', {'error': 'Invalid credentials'})

        elif user_type == 'doctor':
            try:
                doctor = Doctor.objects.get(email=username)
                if doctor.password == password:
                    # Redirect to doctor login page with available patients
                    patients = Patient.objects.all()
                    return render(request, 'doctor_login.html', {'patients': patients, 'doctor': doctor})
                else:
                    return render(request, 'login.html', {'error': 'Invalid credentials'})
            except Doctor.DoesNotExist:
                return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def patient_login(request):
    return render(request, 'patient_login.html')

def doctor_login(request):
    return render(request, 'doctor_login.html')


def register_patient(request):
    if request.method == 'POST':
        # Handle patient registration logic here
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        patient = Patient(
            name=name,
            email=email,
            password=password,
            age=age,
            gender=gender,
            address=address,
            phone=phone
        )
        patient.save()
        return redirect('patient_login')
        # pass
    return render(request, 'register_patient.html')

def register_doctor(request):
    if request.method == 'POST':
        # Handle doctor registration logic here
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        specialization = request.POST.get('specialization')
        experience = request.POST.get('experience')
        phone = request.POST.get('phone')

        doctor = Doctor.objects.create(
            name=name,
            email=email,
            password=password,
            specialization=specialization,
            experience=experience,
            phone=phone
        )
        doctor.save()
        return redirect('doctor_login')
        # pass
    return render(request, 'register_doctor.html')

def get_doctors(request):
    doctors = Doctor.objects.all().values()
    return JsonResponse(list(doctors), safe=False)

def get_patients(request):
    patients = Patient.objects.all().values()
    return JsonResponse(list(patients), safe=False)



def schedule_appointment(request):
    if request.method == 'GET':
        doctor_id = request.GET.get('doctor')
        doctor = Doctor.objects.get(id=doctor_id)
        patient_id = request.GET.get('patient_id')
        return render(request, 'schedule_appointment.html', {'doctor': doctor, 'patient_id': patient_id})

    if request.method == 'POST':
        doctor_id = request.POST.get('doctor_id')
        patient_id = request.POST.get('patient_id')
        appointment_time = request.POST.get('appointment_time')

        doctor = Doctor.objects.get(id=doctor_id)
        patient = Patient.objects.get(id=patient_id)
        doctor.phone = '9555265798'
        # Generate WhatsApp meeting link
        whatsapp_message = f"Appointment with Dr. {doctor.name} on {appointment_time}. Please confirm."
        whatsapp_link = f"https://wa.me/{doctor.phone}?text={requests.utils.quote(whatsapp_message)}"
        appointment = Appointment(
            doctor=doctor,
            patient=patient,
            appointment_time=appointment_time
        )
        appointment.save()
        return render(request, 'appointment_confirmation.html', {'whatsapp_link': whatsapp_link})

    return render(request, 'schedule_appointment.html')
