from django.urls import path
from .views import list_books, register, LibraryDetailView, LoginView, LogoutView, Register

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library'),
    path("books/", list_books, name = "books-list"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('register/', Register.as_view(), name='register'),
    path('register/', register, name='register')
    # path('admin-view/', admin_view, name='admin_view'),
    # path('librarian-view/', librarian_view, name='librarian_view'),
    # path('member-view/', member_view, name='member_view'),
]