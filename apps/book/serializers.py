from rest_framework import serializers
from apps.account.serializers import AccountUpdateSerializer
from .models import Category, Book, MyBook


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class BookListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ['id', 'author', 'title', 'image', 'category', 'price']


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class MyBookListSerializer(serializers.ModelSerializer):
    account = AccountUpdateSerializer()
    book = BookListSerializer()
    class Meta:
        model = Book
        fields = ['id', 'account', 'book']