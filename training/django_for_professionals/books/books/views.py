from django.views.generic import ListView, DetailView
from .models import Book


class BookListView(ListView):
    template_name = 'books/book_list.html'
    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.order_by('-author')
    

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'

for book in Book.objects.all():
    print(book.title)