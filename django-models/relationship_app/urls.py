from django.urls import path
from .views import LibraryDetailView, list_books

urlpatterns = [
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library'),
    path("books/", list_books, name = "books-list"),
    # path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    # path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    # path('register/', views.register, name='register'),
    # path('admin-view/', admin_view, name='admin_view'),
    # path('librarian-view/', librarian_view, name='librarian_view'),
    # path('member-view/', member_view, name='member_view'),
]