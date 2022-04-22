from rest_framework import serializers
from .models import MedPatient


class MedPatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedPatient
        fields = [
            'user',
            'pk',
            'firstname',
            'lastname',
            'nid',
            'phonenumber',
            'email',
            'doctor',
        ]