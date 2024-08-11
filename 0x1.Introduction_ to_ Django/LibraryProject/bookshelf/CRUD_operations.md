## To perform CRUD ```(CREATE, RETRIEVE, UPDATE, DELETE)``` operations using the model.
### The following syntax are used.  

**Create a Book instance**
```
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=2024)
```

**Retrieve a Book record instance**
```Book.objects.get(title="1984")```
> Output: Book: Book object (1)>
**OR**
```book.title```
> Output: '1984'

**Update a Book record instance**
```book.title = "Nineteen Eighty-Four"```

**Delete a Book record instance**
```book.delete()```
Output: (1, {'bookshelf.Book': 1})