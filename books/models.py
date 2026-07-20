from django.db import models
# models function like objects with various properties

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()
    publisher = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=13, unique=True, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    publisher = models.CharField(max_length=200, blank=True)
    year_published = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=100)
    copies_sold = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
