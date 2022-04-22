from rest_framework.permissions import BasePermission

class UserOnlyPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
            return obj.user == request.user