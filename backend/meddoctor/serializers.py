from rest_framework import serializers
from .models import MedDoctor


class MedDoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedDoctor
        fields = [
            'user',
            'pk',
            'firstname',
            'lastname',
            'nid',
            'phonenumber',
            'email',
        ]