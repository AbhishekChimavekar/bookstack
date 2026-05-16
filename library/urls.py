from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet
from .auth_views import RegisterView, ChangePasswordView

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"loans", LoanViewSet)

urlpatterns = [
    path("", include(router.urls)),

    # Auth endpoints
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
    path("auth/change-password/", ChangePasswordView.as_view(), name="auth-change-password"),
]
