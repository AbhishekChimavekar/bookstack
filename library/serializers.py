from rest_framework import serializers
from .models import Book, Loan


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "isbn",
            "available_copies",
            "created_at",
            "updated_at",
        ]


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = [
            "id",
            "book",
            "borrower_name",
            "borrower_email",
            "start_date",
            "due_date",
            "returned",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        start_date = attrs.get("start_date")
        due_date = attrs.get("due_date")

        if start_date and due_date and due_date <= start_date:
            raise serializers.ValidationError(
                "Due date must be after start date."
            )

        return attrs
