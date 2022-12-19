from django.db import models

# Create your models here.

class Prescription (models.Model):
    prescription_id = id
    prescription_patient = models.CharField(max_length=150, name='Patient Name')
    prescription_doctor = models.CharField(max_length=150, name='Doctor Name')
    