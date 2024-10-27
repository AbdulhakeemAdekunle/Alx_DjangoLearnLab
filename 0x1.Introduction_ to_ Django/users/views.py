from typing import Any
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User, Permission
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView, CreateView
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

# Create your views here.

user = User.objects.get(username='newuser')
content_type = ContentType.objects.get_for_model(Book)
permission = Permission.objects.get(codename='view_book', content_type=content_type)
user.user_permissions.add(permission)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'login.html'

@login_required(login_url='login')
def product(request):
    return render(request, 'product.html')
    # return redirect('login')

def index(request):
    return render(request, 'index.html')

def message(request):
    return HttpResponse("This is a simple message view")

class MyView(TemplateView):
    model = Book
    template_name = 'index.html'

@login_required(login_url='login')
def dynamic(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'index.html', context)

@permission_required('relationship_app.view_book', login_url='login')
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        return render (request, 'book_list.html', {'books': books})
    
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'

# user.first_name = 'abdulhakeem'
# user.last_name = 'yisa'
# user.save()

# content_type = ContentType.objects.get_for_model(Book)
# permission = Permission.objects.create(codename='can_publish', name='Can Publish Posts', content_type = content_type)

# auser = authenticate(username='abdul', password='Harkym@123')

# user.has_perm('relationship_app.view_book')
# user.has_perm('relationship_app.change_book')
# user.has_perm('relationship_app.add_book')
# user.has_perm('relationship_app.delete_book')

# user.groups.set(['group_list'])
# user.groups.add()
# user.groups.remove()
# user.groups.clear()
# user.user_permissions = permission

def my_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        books = Book.objects.all()
        context = {'books': books}
        if user is not None:
            login(request, user)
            return render(request, 'product.html', context)
        else:
            return redirect('login')
    return render(request, 'login.html')
