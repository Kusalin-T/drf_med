from rest_framework import generics, authentication, permissions

from .models import MedDoctor
from .serializers import MedDoctorSerializer

class MedDoctorListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedDoctor.objects.all()
    serializer_class = MedDoctorSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

meddoctor_listcreate_view = MedDoctorListCreateAPIView.as_view()

class MedDoctorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedDoctor.objects.all()
    serializer_class = MedDoctorSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

meddoctor_retrieveupdatedestroy_view = MedDoctorRetrieveUpdateDestroyAPIView.as_view()