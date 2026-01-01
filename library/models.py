from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    available_copies = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrower_name = models.CharField(max_length=30)
    borrower_email = models.EmailField(blank=True, null=True)
    start_date = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.book} - {self.borrower_name}"
