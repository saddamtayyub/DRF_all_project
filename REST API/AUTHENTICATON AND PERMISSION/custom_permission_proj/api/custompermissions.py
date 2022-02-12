from rest_framework.permissions import BasePermission


class MyPerms(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
