from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView as Login, LogoutView as Logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy
from .models import Library, Book, UserProfile

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

def check_admin_role(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Admin'

def check_librarian_role(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Librarian'

def check_member_role(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Member'

@login_required
@user_passes_test(check_admin_role)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(check_librarian_role)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(check_member_role)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')