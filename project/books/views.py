import datetime

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from .forms import CreateReaderForm
from .models import Book, Reader


class ReaderListView(View):
    def get(self, request):
        readers = Reader.objects.all()
        return render(request, "books/index.html", {"readers": readers, "title": "Readers"})


class ReaderCreateView(View):
    def get(self, request):
        return render(request, "books/reader_create.html", {"title": "Create reader"})

    def post(self, request):
        form = CreateReaderForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()

        return redirect(reverse("reader-list"))


class ReaderDetailView(View):
    queryset = Book.objects.select_related("author").select_related("reader")

    def get(self, request, pk):
        try:
            reader = Reader.objects.get(pk=pk)
        except Reader.DoesNotExist:
            return HttpResponse(status=404, content="reader not found")

        books = self.queryset.filter(reader=reader)

        return render(request, "books/reader_detail.html", {"reader": reader, "books": books, "title": "Reader"})

    def post(self, request, pk):
        book_id = request.POST.get("book_id")
        book = self.queryset.get(pk=book_id)

        book.status = "in_stock"
        book.reader = None
        book.date_hand_in = datetime.datetime.utcnow()
        book.date_deliver = None
        book.save()

        return redirect(reverse("reader-detail", kwargs={"pk": pk}))


class BookView(View):
    queryset = Book.objects.select_related("author").select_related("reader").all()

    def get(self, request):
        books_on_delivery = self.queryset.filter(status="on_delivery")
        books_in_stock = self.queryset.filter(status="in_stock")
        readers = Reader.objects.all()

        return render(
            request,
            "books/books.html",
            {
                "title": "Books",
                "books_on_delivery": books_on_delivery,
                "books_in_stock": books_in_stock,
                "readers": readers,
            },
        )

    def post(self, request):
        book_id = request.POST.get("book_id")
        reader_id = request.POST.get("reader_id")

        book = self.queryset.get(pk=book_id)
        reader = Reader.objects.get(pk=reader_id)

        book.reader = reader
        book.status = "on_delivery"
        book.date_deliver = datetime.datetime.utcnow()
        book.date_hand_in = None

        book.save()

        return redirect(reverse("book"))
