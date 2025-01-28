from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    """Проверка на наличие прав автора"""

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False


class IsAdmin(permissions.BasePermission):
    """Проверка на наличие роли "admin"""

    def has_permission(self, request, view):
        return request.user.role == "admin"


class IsUser(permissions.BasePermission):
    """Проверка на наличие роли "user"""

    def has_permission(self, request, view):
        return request.user.role == "user"
