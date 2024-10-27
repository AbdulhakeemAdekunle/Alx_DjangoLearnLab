from django.shortcuts import render
from rest_framework.generics import ListAPIView
from api.models import Book
from api.serializers import BookSerializer

# Create your views here.

# book-list view that displays the list of books in db based of BookSerializer
class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer