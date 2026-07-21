from books.models import Author, Book

# create dummy authors first
author1, _ = Author.objects.get_or_create(first_name='Robert', last_name='Martin')
author2, _ = Author.objects.get_or_create(first_name='Gang', last_name='of Four')

# create books with authors
book1, _ = Book.objects.get_or_create(ISBN='9780132350884', defaults={
    'title': 'Clean Code',
    'price': 35.99,
    'genre': 'Technology',
    'publisher': 'Prentice Hall',
    'year_published': 2008,
    'copies_sold': 500,
    'description': 'A handbook of agile software craftsmanship.',
    'author': author1,
})

book2, _ = Book.objects.get_or_create(ISBN='9780201633610', defaults={
    'title': 'Design Patterns',
    'price': 44.99,
    'genre': 'Technology',
    'publisher': 'Addison-Wesley',
    'year_published': 1994,
    'copies_sold': 300,
    'description': 'Elements of reusable object-oriented software.',
    'author': author2,
})

book3, _ = Book.objects.get_or_create(ISBN='9781119986645', defaults={
    'title': 'Java for Dummies',
    'price': 12.35,
    'genre': 'Technology',
    'publisher': 'Wiley & Sons',
    'year_published': 2012,
    'copies_sold': 1622,
    'description': 'Coder\'s resource for programming with Java.',
    'author': author1,
})