from rest_framework import serializers
from .models import MedAdmin

class MedAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedAdmin
        fields = [
            'firstname',
            'lastname',
            'nid',
            'phonenumber',
            'email',
        ]