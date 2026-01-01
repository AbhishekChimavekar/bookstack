from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Book, Loan
from .serializers import BookSerializer, LoanSerializer



class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer

class AvailableBookListView(generics.ListAPIView):
    queryset = Book.objects.filter(available_copies__gt=0).order_by("title")
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all().order_by("-start_date")
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        book = serializer.validated_data["book"]

        if book.available_copies <= 0:
            # Stop creation if no stock
            raise ValidationError("No available copies for this book.")

        # Decrement stock and save both Book and Loan
        book.available_copies -= 1
        book.save()
        serializer.save()

    
class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        was_returned = instance.returned  # state before update

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        updated_loan = serializer.save()

        # If it was not returned before but now is returned, add one copy back
        if not was_returned and updated_loan.returned:
            book = updated_loan.book
            book.available_copies += 1
            book.save()

        return Response(serializer.data)

