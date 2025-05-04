from django.shortcuts import render, redirect
from .models import Appointment
from .models import Doctor
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import AppointmentSerializer
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

class AppointmentAPIView(APIView):
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def base (request): 
    return render(request, 'base.html')
def home(request): 
    return render(request, 'home.html')
def about(request): 
    return render(request, 'about.html')
def services(request): 
    return render(request, 'services.html')
def doctors(request):
    all_doctors = Doctor.objects.all()
    return render(request, 'doctors.html', {'doctors': all_doctors})

def appointment(request):
    if request.method == 'POST':
        name = request.POST['name']
        contact = request.POST['contact']
        email= request.POST['email']
        department = request.POST['department']
        preferred_date = request.POST.get('preferred_date')
        preferred_time = request.POST.get('preferred_time')




        # Send email
        subject = 'New Appointment Booking'
        message = f'Appointment details:\nName: {name}\nEmail: {email}\nPhone: {contact}\nPreferred Date: {preferred_date}\nPreferred Time: {preferred_time}'
        hospital_email = 'dhanushsri890@gmail.com'  # Replace with your hospital email
        recipient_list = [hospital_email]
        send_mail(subject, message, hospital_email, recipient_list)
        # Patient confirmation email
        confirmation_subject = 'Appointment Confirmation - Harmony Care Hospital'
        confirmation_message = f'''
        Dear {name},
        Thank you for booking an appointment at Harmony Care Hospital.
        We have received your request for {preferred_date} {preferred_time}.
        Our team will contact you soon to confirm your appointment.
        Best regards,
        Harmony Care Hospital'''
        send_mail(confirmation_subject, confirmation_message, hospital_email, [email])
        return render(request, 'thank_you.html')

    return render(request, 'appointment.html')




def contact(request):
        return render(request, 'contact.html')

def success(request):
    return render(request, 'success.html')