from rest_framework import generics, authentication, permissions

from .models import MedAdmin
from .serializers import MedAdminSerializer



class MedAdminListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

medadmin_listcreate_view = MedAdminListCreateAPIView.as_view()

class MedAdminRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

medadmin_retrieveupdatedestroy_view = MedAdminRetrieveUpdateDestroyAPIView.as_view()
