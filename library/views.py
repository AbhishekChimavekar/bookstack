from rest_framework import viewsets, filters
from rest_framework.decorators import action
from django.db import transaction
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['author']
    search_fields = ['title', 'author', 'isbn']
    ordering_fields = ['title', 'created_at']

    @action(detail=False, methods=["get"])
    def available(self, request):
        books = Book.objects.filter(available_copies__gt=0).order_by("title")
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all().order_by("-start_date")
    serializer_class = LoanSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['returned', 'book']
    search_fields = ['borrower_name', 'borrower_email']
    ordering_fields = ['start_date', 'due_date']

    @transaction.atomic
    def perform_create(self, serializer):
        book = serializer.validated_data["book"]
        
        if book.available_copies <= 0:
            raise ValidationError("No available copies for this book.")
        
        book.available_copies -= 1
        book.save()
        serializer.save()

    @transaction.atomic
    def perform_update(self, serializer):
        instance = self.get_object()
        was_returned = instance.returned
        updated_loan = serializer.save()
        
        if not was_returned and updated_loan.returned:
            book = updated_loan.book
            book.available_copies += 1
            book.save()
            