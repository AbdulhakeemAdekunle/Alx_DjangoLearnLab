from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Library, Book

# Create your views here.

def books_list(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"