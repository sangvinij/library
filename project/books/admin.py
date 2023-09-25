from django.contrib import admin

from .models import Author, Book, Reader


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "reader", "status", "date_deliver", "date_hand_in")
    list_filter = ("status",)
    search_fields = ("title", "author")


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "patronymic")
    search_fields = ("first_name", "last_name", "patronymic")


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "patronymic")
    search_fields = ("first_name", "last_name", "patronymic")
