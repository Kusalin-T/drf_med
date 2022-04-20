from rest_framework import generics

from .models import MedAdmin
from .serializers import MedAdminSerializer

class MedAdminDetailAPIView(generics.RetrieveAPIView):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer

medadmin_detail_view = MedAdminDetailAPIView.as_view()