from django.db import models

# Create your models here.


# Create a Book model with fields: id, title, author
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)