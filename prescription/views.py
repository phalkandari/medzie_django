from django.shortcuts import render
from rest_framework.generics import ListAPIView
from prescription.models import Prescription
from rest_framework.response import Response

from prescription.serializers import PrescriptionListSerializer




class PrescriptionListView(ListAPIView):

    serializer_class = PrescriptionListSerializer

    def get_queryset(self):
        return Prescription.objects.filter(patient=self.request.user)


