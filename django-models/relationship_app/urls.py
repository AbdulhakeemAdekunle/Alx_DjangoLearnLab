from django.urls import path
from .views import list_books, LibraryDetailView, LogoutView, LoginView

urlpatterns = [
    path("", LibraryDetailView.as_view(), name='library'),
    path("book", list_books, name = "books-list"),
    path('login/', LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register/', views.register, name='register'),
]