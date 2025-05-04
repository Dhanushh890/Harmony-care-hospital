from django.db import models

# Department choices for reuse
DEPARTMENTS = [
    ('Cardiology', 'Cardiology'),
    ('Orthopedics', 'Orthopedics'),
    ('Pediatrics', 'Pediatrics'),
    ('General Surgery', 'General Surgery'),
    ('Dermatology', 'Dermatology'),
]

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    department = models.CharField(max_length=255)  # Ensure this field exists
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='doctor_photos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20)
    email = models.EmailField()  # ← Make sure this exists
    department = models.CharField(max_length=100)
    preferred_date = models.DateField()
    preferred_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

