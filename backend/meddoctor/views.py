from rest_framework import generics, authentication, permissions

from .models import MedDoctor
from .serializers import MedDoctorSerializer
from .permissions import UserOnlyPermission

class MedDoctorListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedDoctor.objects.all()
    serializer_class = MedDoctorSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

meddoctor_listcreate_view = MedDoctorListCreateAPIView.as_view()

class MedDoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedDoctor.objects.all()
    serializer_class = MedDoctorSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

meddoctor_retrieveupdatedestroy_view = MedDoctorRetrieveUpdateDestroyAPIView.as_view()

class MedDoctorRetrieveAPIView(generics.RetrieveAPIView, UserOnlyPermission):
    queryset = MedDoctor.objects.all()
    serializer_class = MedDoctorSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [UserOnlyPermission|permissions.IsAdminUser]

meddoctor_retrieve_view = MedDoctorRetrieveAPIView.as_view()