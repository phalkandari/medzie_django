from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Prescription (models.Model):
    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="prescriptions",
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="issued_prescriptions",
    )
    note = models.TextField()