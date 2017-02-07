from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """custom permissions to only allow owners of object"""
    def has_object_permission(self,request, view, obj):
        if request.method in permissions.SAFE_METHODS:###GET,HEAD,OPTIONS
            return True
        return obj.owner == request.user
