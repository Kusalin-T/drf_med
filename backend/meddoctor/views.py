from rest_framework import generics, authentication, permissions

from .models import MedDoctor
from .serializers import MedDoctorSerializer
from .permissions import UserDoctorRetrievePermission

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

class MedDoctorRetrieveAPIView(generics.RetrieveAPIView, UserDoctorRetrievePermission):
    queryset = MedDoctor.objects.all()
    serializer_class = MedDoctorSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [UserDoctorRetrievePermission|permissions.IsAdminUser]

meddoctor_retrieve_view = MedDoctorRetrieveAPIView.as_view()