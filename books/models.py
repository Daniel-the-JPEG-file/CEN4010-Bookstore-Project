from django.db import models

# Create your models here.

# example model
# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.CharField(max_length=200)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     genre = models.CharField(max_length=100)
#     stock = models.IntegerField(default=0)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.title

from django.db import models

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


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.CharField(max_length=100, db_column='user_id')
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} rated {self.book.title}: {self.score}/5"


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    user = models.CharField(max_length=100, db_column='user_id')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} on {self.book.title}"