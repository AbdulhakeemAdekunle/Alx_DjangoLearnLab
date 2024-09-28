from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView as Login, LogoutView as Logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse_lazy
from .models import Library, Book

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


class LoginView(Login):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('books-list')

class LogoutView(Logout):
    template_name = 'relationship_app/logout.html'
    success_url = reverse_lazy('login')

class Register(CreateView):
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# # Helper function to check the role
# def check_role(role):
#     def decorator(user):
#         return user.userprofile.role == role
#     return decorator

# # Admin view
# @user_passes_test(check_role('Admin'))
# def admin_view(request):
#     return render(request, 'relationship_app/admin_view.html')

# # Librarian view
# @user_passes_test(check_role('Librarian'))
# def librarian_view(request):
#     return render(request, 'relationship_app/librarian_view.html')

# # Member view
# @user_passes_test(check_role('Member'))
# def member_view(request):
#     return render(request, 'relationship_app/member_view.html')