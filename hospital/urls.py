from django.urls import path
from . import views
from .views import AppointmentAPIView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('api/appointment/', AppointmentAPIView.as_view(), name='api_appointment'),
    path('success/', views.success, name='success'),

]
