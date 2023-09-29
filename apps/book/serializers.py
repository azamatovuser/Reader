from rest_framework import serializers
from apps.account.serializers import AccountUpdateSerializer
from .models import Book, MyBook


class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'image']


class MyBookListSerializer(serializers.ModelSerializer):
    account = AccountUpdateSerializer()
    book = BookListSerializer()
    class Meta:
        model = Book
        fields = ['id', 'account', 'book']