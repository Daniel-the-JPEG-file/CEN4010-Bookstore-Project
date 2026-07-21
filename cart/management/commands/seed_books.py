from django.core.management.base import BaseCommand
from cart.models import Book

class Command(BaseCommand):
    help = 'Seed the database with 10 test books'

    def handle(self, *args, **kwargs):
        books = [
            {"isbn": "9780132350884", "name": "Clean Code", "description": "A handbook of agile software craftsmanship", "price": 35.99, "genre": "Technology", "publisher": "Prentice Hall", "year_published": 2008, "copies_sold": 500},
            {"isbn": "9780201633610", "name": "Design Patterns", "description": "Elements of reusable object-oriented software", "price": 45.99, "genre": "Technology", "publisher": "Addison Wesley", "year_published": 1994, "copies_sold": 300},
            {"isbn": "9780596517748", "name": "JavaScript: The Good Parts", "description": "Unearthing the excellence in JavaScript", "price": 29.99, "genre": "Technology", "publisher": "O'Reilly", "year_published": 2008, "copies_sold": 400},
            {"isbn": "9781491950357", "name": "Python Data Science Handbook", "description": "Essential tools for working with data", "price": 55.99, "genre": "Technology", "publisher": "O'Reilly", "year_published": 2016, "copies_sold": 250},
            {"isbn": "9780134685991", "name": "Effective Java", "description": "Best practices for the Java platform", "price": 49.99, "genre": "Technology", "publisher": "Addison Wesley", "year_published": 2018, "copies_sold": 350},
            {"isbn": "9781617294433", "name": "Deep Learning with Python", "description": "A hands-on guide to deep learning", "price": 59.99, "genre": "Technology", "publisher": "Manning", "year_published": 2017, "copies_sold": 600},
            {"isbn": "9780134494166", "name": "Clean Architecture", "description": "A craftsman's guide to software structure", "price": 39.99, "genre": "Technology", "publisher": "Prentice Hall", "year_published": 2017, "copies_sold": 450},
            {"isbn": "9781492056355", "name": "Designing Data-Intensive Applications", "description": "The big ideas behind reliable and scalable systems", "price": 65.99, "genre": "Technology", "publisher": "O'Reilly", "year_published": 2017, "copies_sold": 700},
            {"isbn": "9780135957059", "name": "The Pragmatic Programmer", "description": "Your journey to mastery", "price": 49.99, "genre": "Technology", "publisher": "Addison Wesley", "year_published": 2019, "copies_sold": 550},
            {"isbn": "9781593279509", "name": "Automate the Boring Stuff with Python", "description": "Practical programming for total beginners", "price": 24.99, "genre": "Technology", "publisher": "No Starch Press", "year_published": 2019, "copies_sold": 800},
        ]

        for book_data in books:
            book, created = Book.objects.get_or_create(isbn=book_data['isbn'], defaults=book_data)
            if created:
                self.stdout.write(f"Created: {book.name}")
            else:
                self.stdout.write(f"Already exists: {book.name}")

        self.stdout.write(self.style.SUCCESS('Done! 10 books seeded.'))