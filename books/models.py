from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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


class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='ratings')
    user = models.CharField(max_length=100, db_column='user_id')
    score = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
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


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True,blank=True,null=True)
    home_address = models.CharField(max_length=255,blank=True,null=True)
    def __str__(self):
        return self.username


class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='credit_cards')
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cardholder_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.cardholder_name} - {self.card_number[-4:]}"