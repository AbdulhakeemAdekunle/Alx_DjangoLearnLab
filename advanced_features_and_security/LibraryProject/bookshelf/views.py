from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import permission_required

# Create your views here.

permission_required('bookshelf.can_view_customer', raise_exception=True) # checks if a user has a view access
def view_customer(request):
    return HttpResponse('You can view customer records') # displays message if the user belongs to the viewers' group

permission_required('bookshelf.can_create_customer', raise_exception=True) # checks if a user has a create access
def create_custome(request):
    return HttpResponse('You can create customer records') # displays message if the user belongs to the editors' group

permission_required('bookshelf.can_edit_customer', raise_exception=True) # checks if a user has a edit access
def edit_customer(request):
    return HttpResponse('You can edit customer records') # displays message if the user belongs to the editors' group

permission_required('bookshelf.can_delete_customer', raise_exception=True) # checks if a user has a delete access
def delete_customer(request):
    return HttpResponse('You can delete customer records') # displays message if the user belongs to the admin group (only admin can delete a user record)
