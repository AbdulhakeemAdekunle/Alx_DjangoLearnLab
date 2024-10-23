from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView as Login, LogoutView as Logout
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from .models import Library, Book, UserProfile
from .forms import BookForm

# Create your views here.

def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a 'success' or 'book list' page
            return redirect('book-list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book-list')  # Redirect to a 'book list' page
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully.")
        return HttpResponseRedirect(reverse('book-list'))  # Redirect to the book list
    return render(request, 'relationship_app/delete_book.html', {'book': book})

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

class LoginView(Login):
    template_name = 'relationship_app/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('books-list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def Admin(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Admin'

def Librarian(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Librarian'

def Member(user):
    return user.is_authenticated and UserProfile.objects.get(user=user).role == 'Member'

@login_required
@user_passes_test(Admin)
def Admin(request):
    return HttpResponse('Admin page')

@login_required
@user_passes_test(Librarian)
def Librarian(request):
    return HttpResponse('Librarian Page')

@login_required
@user_passes_test(Member)
def Member(request):
    return HttpResponse('Member Page')

@method_decorator(user_passes_test(admin), name='dispatch')
class Admin(TemplateView):
    template_name = 'index.html'