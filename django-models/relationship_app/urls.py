from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path("", LibraryDetailView.as_view(), name='library'),
    path("book", list_books, name = "books-list"),
]