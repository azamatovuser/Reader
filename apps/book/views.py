from rest_framework import generics
from .models import Book, MyBook
from .serializers import BookListSerializer, BookDetailSerializer, MyBookListSerializer
from rest_framework import permissions


class BookListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/book/list/
    queryset = Book.objects.all()
    serializer_class = BookListSerializer


class BookDetailAPIView(generics.RetrieveAPIView):
    # http://127.0.0.1:8000/book/detail/book_id/
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer


class MyBookListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/book/my_list/
    queryset = MyBook.objects.all()
    serializer_class = MyBookListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        account = self.request.user
        return qs.filter(account=account)