from rest_framework.test import APITestCase
from rest_framework import status
from apps.book.serializers import BookListSerializer, \
    BookDetailSerializer, MyBookListSerializer, CategorySerializer
from apps.book.models import Book, MyBook, Category
from apps.account.models import Account
import uuid


class BookListTestCase(APITestCase):
    def setUp(self):
        # Creating data for Book
        self.data_one = Book.objects.create(
            author='data_one',
            title='data_one',
            description='data_one',
            price='99.99'
        )
        self.data_two = Book.objects.create(
            author='data_two',
            title='data_two',
            description='data_two',
            price='99.99'
        )

    def get(self):
        response = self.client.get('/book/list/')
        serializer_data = BookListSerializer([self.data_one, self.data_two], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class BookDetailTestCase(APITestCase):
    def setUp(self):
        # Creating data for Book
        self.data_one = Book.objects.create(
            author='data_one',
            title='data_one',
            description='data_one',
            price='99.99'
        )

    def get(self):
        response = self.client.get(f'/book/detail/{self.data_one.id}/')
        serializer_data = BookDetailSerializer(self.data_one).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)