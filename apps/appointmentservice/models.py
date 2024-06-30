from django.db import models

# Create your models here.
class Appointment(models.Model):

    id = models.CharField(max_length=64, primary_key=True, blank=False)
    patient_id = models.CharField(max_length=64, null=False, blank=False)
    doctor_id = models.CharField(max_length=64, null=False, blank=False)
    date = models.DateTimeField()
    status = models.CharField(max_length=64, null=False, blank=False, default='pending')
    type = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

