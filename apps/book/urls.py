from django.urls import path
from .views import BookListAPIView, MyBookListAPIView, BookDetailAPIView

app_name = 'book'

urlpatterns = [
    path('list/', BookListAPIView.as_view()),
    path('detail/<int:pk>/', BookDetailAPIView.as_view()),
    path('my_list/', MyBookListAPIView.as_view()),
]