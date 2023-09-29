from rest_framework import generics
from .models import Book, MyBook
from .serializers import BookListSerializer, MyBookListSerializer


class BookListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/book/list/
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class MyBookListAPIView(generics.ListAPIView):
    queryset = MyBook.objects.all()
    serializer_class = MyBookListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        account = self.request.user
        return qs.filter(account=account)