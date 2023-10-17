from django.db import models
from apps.account.models import Account


class Timestamp(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Category(Timestamp):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Book(Timestamp):
    author = models.CharField(max_length=221)
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='book_images/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    file = models.FileField(upload_to='book_files/', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=True)

    def __str__(self):
        return self.title


class MyBook(Timestamp):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['account', 'book']

    def __str__(self):
        return f"{self.account}'s saved book -{self.book}"