from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView, register

urlpatterns = [
    path("", LibraryDetailView.as_view(), name='library'),
    path("book", list_books, name = "books-list"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
]