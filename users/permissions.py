from rest_framework import permissions

class IsSubscribed(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user and (request.user.permission_class == 'SUBSCRIBED'):
            return True
        else:
            return False
