from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

# Create your views here.

# BookViewSet that handles CRUD operations for Book model on GET, PUT, UPDATE, DELETE requests 
class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer