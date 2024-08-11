from bookshelf.models import Book
book = Books.objects.filter(title="Nineteen Eighty-Four")
book.delete()
```(0, {})```