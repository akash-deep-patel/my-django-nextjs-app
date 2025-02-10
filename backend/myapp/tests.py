from django.test import TestCase
from .models import Doctor, Patient, Appointment

class AppointmentModelTest(TestCase):

    def setUp(self):
        self.doctor = Doctor.objects.create(name="Dr. Smith", specialization="Cardiology")
        self.patient = Patient.objects.create(name="John Doe", email="john@example.com")

    def test_appointment_creation(self):
        appointment = Appointment.objects.create(
            doctor=self.doctor,
            patient=self.patient,
            appointment_time="2023-10-01 10:00:00",
            is_online=True
        )
        self.assertEqual(appointment.doctor, self.doctor)
        self.assertEqual(appointment.patient, self.patient)
        self.assertTrue(appointment.is_online)

    def test_appointment_offline_choice(self):
        appointment = Appointment.objects.create(
            doctor=self.doctor,
            patient=self.patient,
            appointment_time="2023-10-01 11:00:00",
            is_online=False
        )
        self.assertFalse(appointment.is_online)