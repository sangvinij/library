from django.urls import path

from .views import ReaderListView, ReaderDetailView, ReaderCreateView, BookView

urlpatterns = [
    path("", ReaderListView.as_view(), name="reader-list"),
    path("readers/create", ReaderCreateView.as_view(), name="reader-create"),
    path("readers/<int:pk>", ReaderDetailView.as_view(), name="reader-detail"),
    path("books/", BookView.as_view(), name="book"),
]
