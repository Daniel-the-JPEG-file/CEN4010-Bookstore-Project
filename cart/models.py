from django.db import models

class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    year_published = models.IntegerField()
    copies_sold = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class CartItem(models.Model):
    user_id = models.IntegerField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user_id} - {self.book.name}"