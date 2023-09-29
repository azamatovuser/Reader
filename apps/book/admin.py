from django.contrib import admin
from .models import Book, MyBook


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')


@admin.register(MyBook)
class MyBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'book')