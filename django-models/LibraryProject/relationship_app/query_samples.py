from .models import Book, Author, Library, Librarian

#This script contains:
#Creation of instances for all the models
#The query for each of the following of relationship

# Create an Author instance
author = Author.objects.create(name="Blessing Malik")

# Create a Book instance
book = Book.objects.create(title="Nineteen Eigthy-Four", author=author)

# Create a Library instance
library = Library.objects.create(name="Fred Swaniker Library Complex")

# Create a Librarian instance
librarian = Librarian.objects.create(name="Nungari Nguru", library=library)

#Query all books by a specific author.
Book.objects.filter(author__name="author_name")


# List all books in a library.
library = Library.objects.get(name="library_name")
books_in_library = library.books.all()

# Retrieve the librarian for a library.
Librarian.objects.get(library__name = "library_name")