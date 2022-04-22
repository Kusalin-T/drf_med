from rest_framework import generics, authentication, permissions

from .models import MedAdmin
from .serializers import MedAdminSerializer
from .permissions import UserOnlyPermission



class MedAdminListCreateAPIView(generics.ListCreateAPIView):

    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

medadmin_listcreate_view = MedAdminListCreateAPIView.as_view()

class MedAdminRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

medadmin_retrieveupdatedestroy_view = MedAdminRetrieveUpdateDestroyAPIView.as_view()

class MedAdminRetrieveAPIView(generics.RetrieveAPIView, UserOnlyPermission):
    queryset = MedAdmin.objects.all()
    serializer_class = MedAdminSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [UserOnlyPermission|permissions.IsAdminUser]

medadmin_retrieve_view = MedAdminRetrieveAPIView.as_view()
