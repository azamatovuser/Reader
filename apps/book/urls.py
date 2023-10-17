from django.urls import path
from .views import BookListAPIView, MyBookListAPIView, \
    BookDetailAPIView, MyBookRetrieveDestroyAPIView, \
    CategoryListAPIView, MyBookCreateAPIView

app_name = 'book'

urlpatterns = [
    path('category/list/', CategoryListAPIView.as_view()),
    path('list/', BookListAPIView.as_view()),
    path('detail/<int:pk>/', BookDetailAPIView.as_view()),
    path('my_list/', MyBookListAPIView.as_view()),
    path('my_list/create/', MyBookCreateAPIView.as_view()),
    path('my_list/detail/<int:pk>/', MyBookRetrieveDestroyAPIView.as_view()),
]