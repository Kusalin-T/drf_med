from rest_framework import generics, authentication, permissions

from .models import MedPatient
from .serializers import MedPatientSerializer
from .permissions import UserOnlyPermission

class MedPatientListCreateAPIView(generics.ListCreateAPIView):
    queryset = MedPatient.objects.all()
    serializer_class = MedPatientSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

medpatient_listcreate_view = MedPatientListCreateAPIView.as_view()

class MedPatientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedPatient.objects.all()
    serializer_class = MedPatientSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

medpatient_retrieveupdatedestroy_view = MedPatientRetrieveUpdateDestroyAPIView.as_view()

class MedPatientRetrieveAPIView(generics.RetrieveAPIView, UserOnlyPermission):
    queryset = MedPatient.objects.all()
    serializer_class = MedPatientSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [UserOnlyPermission|permissions.IsAdminUser]

medpatient_retrieve_view = MedPatientRetrieveAPIView.as_view()