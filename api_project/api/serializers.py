from rest_framework import serializers
from .models import Book

# BookSerializer class that gets render on api endpoint for GET request: api/books
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' # all Book fields are displayed