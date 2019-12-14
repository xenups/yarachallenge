from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from challenge.models import Post


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
