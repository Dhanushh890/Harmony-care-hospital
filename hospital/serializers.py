# hospital/serializers.py

from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['name', 'contact_number', 'department', 'preferred_datetime']
