from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, LoanViewSet
from .auth_views import RegisterView

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"loans", LoanViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="auth-register"),
]
