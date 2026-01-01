from django.urls import path
from .views import (
    BookListCreateView,
    BookDetailView,
    LoanListCreateView,
    LoanDetailView,
    AvailableBookListView
)

urlpatterns = [
    path("books/available/", AvailableBookListView.as_view(), name="available-book-list"),
    path("books/", BookListCreateView.as_view(), name="book-list-create"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("loans/", LoanListCreateView.as_view(), name="loan-list-create"),
    path("loans/<int:pk>/", LoanDetailView.as_view(), name="loan-detail"),
]
