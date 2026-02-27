from rest_framework import viewsets
from rest_framework.decorators import action
from models import Book, Loan
from serializers import BookSerializer, LoanSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("title")
    serializer_class = BookSerializer
    
    @action(detail=False, methods=["get"])
    def available(self, request):
        books = Book.objects.filter(available_copies__gt=0).order_by("title")
        serializer = self.get_serializer(books, many=True)
        return Response(serializer.data)
    