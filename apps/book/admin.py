from django.contrib import admin
from .models import Category, Book, MyBook


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title')


@admin.register(MyBook)
class MyBookAdmin(admin.ModelAdmin):
    list_display = ('id', 'account', 'book')