from rest_framework.test import APITestCase
from rest_framework import status
from apps.book.serializers import MyBookListSerializer
from apps.book.models import Book, MyBook
from apps.account.models import Account
import uuid


class MyBookListTestCase(APITestCase):
    def setUp(self):
        # Creating data for MyBook
        self.user = Account.objects.create_user(
            username=f'account_data_{uuid.uuid4()}',
            password='account_data',
        )
        self.book_data_one = Book.objects.create(
            author='book_data_one',
            title='book_data_one',
            description='book_data_one',
            price='99.99'
        )
        self.book_data_two = Book.objects.create(
            author='book_data_two',
            title='book_data_two',
            description='book_data_two',
            price='99.99'
        )

        # Inserting data into MyBook
        self.mybook_data_one = MyBook.objects.create(
            account=self.user,
            book=self.book_data_one
        )
        self.mybook_data_two = MyBook.objects.create(
            account=self.user,
            book=self.book_data_two
        )

    def get(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/book/my_list/')
        serializer_data = MyBookListSerializer([self.mybook_data_one, self.mybook_data_two], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)


class MyBookRetrieveDestroyTestCase(APITestCase):

    def setUp(self):
        self.user = Account.objects.create_user(username='testuser', password='testpass')
        self.other_user = Account.objects.create_user(username='otheruser', password='otherpass')

        self.book = Book.objects.create(
            author='book_author',
            title='book_title',
            description='book_description',
            price='99.99'
        )
        self.mybook = MyBook.objects.create(account=self.user, book=self.book)

    def test_retrieve_mybook_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.get(f'/book/my_list/detail/{self.mybook.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], self.mybook.id)

    def test_retrieve_mybook_unauthorized(self):
        self.client.force_authenticate(self.other_user)
        response = self.client.get(f'/book/my_list/detail/{self.mybook.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_mybook_authenticated(self):
        self.client.force_authenticate(self.user)
        response = self.client.delete(f'/book/my_list/detail/{self.mybook.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_mybook_unauthorized(self):
        self.client.force_authenticate(self.other_user)
        response = self.client.delete(f'/book/my_list/detail/{self.mybook.id}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_retrieve_delete_without_authentication(self):
        response = self.client.get(f'/book/my_list/detail/{self.mybook.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        response = self.client.delete(f'/book/my_list/detail/{self.mybook.id}/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)