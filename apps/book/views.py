from rest_framework import generics
from .models import Category, Book, MyBook
from .serializers import BookListSerializer, BookDetailSerializer, \
    MyBookListSerializer, CategorySerializer
from rest_framework import permissions
from .permissions import IsOwnUserOrReadOnly
from django.shortcuts import Http404
from rest_framework.exceptions import NotFound


class CategoryListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/book/category/list/
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class BookListAPIView(generics.ListAPIView):
    # http://127.0.0.1:8000/book/list/
    queryset = Book.objects.all()
    serializer_class = BookListSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        if search:
            return qs.filter(title__icontains=search)
        if category:
            return qs.filter(category__title__icontains=category)
        return qs


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


class MyBookRetrieveDestroyAPIView(generics.RetrieveDestroyAPIView):
    # http://127.0.0.1:8000/book/my_list/detail/book_id/
    queryset = MyBook.objects.all()
    serializer_class = MyBookListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnUserOrReadOnly]

    def get_object(self):
        mybook_id = self.kwargs.get('pk')

        try:
            user_book = MyBook.objects.get(id=mybook_id, account=self.request.user)
            return user_book
        except MyBook.DoesNotExist:
            raise NotFound(detail="not found")