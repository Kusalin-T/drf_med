from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import MedAdmin


class MedAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedAdmin
        fields = [
            'pk',
            'firstname',
            'lastname',
            'nid',
            'phonenumber',
            'email',
        ]