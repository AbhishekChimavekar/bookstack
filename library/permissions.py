from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrReadOnly(BasePermission):
    """
    Admins (is_staff=True) get full write access.
    Authenticated users get read-only access (GET, HEAD, OPTIONS).
    Unauthenticated requests are denied entirely.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff