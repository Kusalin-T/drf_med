from rest_framework import generics, permissions

from .models import MedAdmin
from .serializers import MedAdminSerializer



class MedAdminListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer
    permission_classes = [permissions.IsAuthenticated]

medadmin_listcreate_view = MedAdminListCreateAPIView.as_view()

class MedAdminRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer

medadmin_retrieveupdatedestroy_view = MedAdminRetrieveUpdateDestroyAPIView.as_view()
