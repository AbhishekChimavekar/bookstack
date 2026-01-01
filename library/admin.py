from django.contrib import admin
from .models import Book, Loan


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "author", 
        "isbn", 
        "available_copies"
    )


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "borrower_name",
        "borrower_email",
        "start_date",
        "due_date",
        "returned",
    )
