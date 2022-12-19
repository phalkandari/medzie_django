from django import forms
from django.db import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from prescription.models import Prescription
from django.shortcuts import get_object_or_404

# Create your models here.

User = get_user_model()


# patient_group, created = Group.objects.get_or_create(name="Patient")
# pharmacist_group, created = Group.objects.get_or_create(name="Pharmacist")
# doctor_group, created = Group.objects.get_or_create(name="Doctor")

# patient_group.permissions.set('prescription.view_prescription')