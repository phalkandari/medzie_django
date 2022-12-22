from rest_framework import serializers
from prescription.models import Prescription
from user.serializers import UserProfileSerializer

class PrescriptionListSerializer(serializers.ModelSerializer):

    doctor = UserProfileSerializer()

    class Meta:
        model = Prescription
        fields = ['id', 'doctor', 'patient', 'note']