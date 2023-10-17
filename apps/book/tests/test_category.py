from rest_framework.test import APITestCase
from rest_framework import status
from apps.book.serializers import CategorySerializer
from apps.book.models import Category
from apps.account.models import Account


class CategoryListTestCase(APITestCase):
    def setUp(self):
        self.category_data_one = Category.objects.create(
            title='data_one'
        )
        self.category_data_two = Category.objects.create(
            title='data_two'
        )

    def get(self):
        response = self.client.get('/book/category/list/')
        serializer_data = CategorySerializer([self.category_data_one, self.category_data_two], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)