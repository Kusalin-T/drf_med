from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from medadmin.models import MedAdmin
from medadmin.serializers import MedAdminSerializer


@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    instance = MedAdmin.objects.all().order_by("?").first()
    data={}
    if instance:
        data = MedAdminSerializer(instance).data

    return Response(data)

