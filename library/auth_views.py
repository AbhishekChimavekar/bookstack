from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from .auth_serializers import RegisterSerializer, ChangePasswordSerializer


class RegisterView(APIView):
    """
    POST /api/auth/register/
    Public endpoint — no authentication required.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Registration successful.",
                    "data": {"username": user.username, "email": user.email},
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "success": False,
                "message": "Registration failed.",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

class ChangePasswordView(APIView):
    """
    POST /api/auth/change-password/
    Requires a valid JWT token.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ChangePasswordSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "success": True,
                    "message": "Password updated successfully.",
                },
                status=status.HTTP_200_OK,
            )
        return Response(
            {
                "success": False,
                "message": "Password change failed.",
                "errors": serializer.errors,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
        