from django.urls import path
from .views import add_book_view, edit_book_view, delete_book_view, list_books, register, LibraryDetailView, LoginView, LogoutView, Register, admin_view, librarian_view, member_view

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library'),
    path("books/", list_books, name = "books-list"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),
    path('add_book/', add_book_view, name='add-book'),
    path('edit_book/<int:pk>/', edit_book_view, name='edit-book'), 
    path('books/delete/<int:pk>/', delete_book_view, name='delete-book'),
]