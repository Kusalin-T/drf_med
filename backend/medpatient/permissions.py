from rest_framework.permissions import BasePermission

class UserPatientRetrievePermission(BasePermission):
    def has_object_permission(self, request, view, obj):
            return ((obj.user == request.user) or (obj.doctor == request.user))