from django.shortcuts import render
from django.http import HttpResponse
from . models import Book, Author, Library, Librarian

# Create your views here.

"""
Implement Function-based View:

Create a function-based view in relationship_app/views.py that lists all books stored in the database.
This view should render a simple text list of book titles and their authors.
"""
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)