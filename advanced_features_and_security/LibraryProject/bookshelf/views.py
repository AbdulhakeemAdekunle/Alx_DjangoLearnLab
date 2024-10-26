from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

# Create your views here.

permission_required('bookshelf.can_view_customer', raise_exception=True) # checks if a user has a view access
def book_list(request):
    return HttpResponse('You can view book records') # displays message if the user belongs to the viewers' group

permission_required('bookshelf.can_create_customer', raise_exception=True) # checks if a user has a create access
def create_book(request):
    return HttpResponse('You can create book records') # displays message if the user belongs to the editors' group

permission_required('bookshelf.can_edit_customer', raise_exception=True) # checks if a user has a edit access
def edit_edit(request):
    return HttpResponse('You can edit book records') # displays message if the user belongs to the editors' group

permission_required('bookshelf.can_delete_customer', raise_exception=True) # checks if a user has a delete access

def delete_book(request):
    return HttpResponse('You can delete book records') # displays message if the user belongs to the admin group (only admin can delete a user record)

def get_book(request):
    # If this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = ExampleForm(request.POST)
        if form.is_valid():
            # process the data in form
            return HttpResponse('created successfully')
        else:
            # if a GET (or any other method) we'll create a blank form
            form = ExampleForm()
        return render(request, 'form_example.html', {'form': form})