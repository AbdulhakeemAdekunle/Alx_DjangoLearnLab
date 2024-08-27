from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from relationship_app.models import Book, Author, Library, Librarian

# Create your views here.

def books_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

class LibraryView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'