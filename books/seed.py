from books.models import Author, Book, Rating, Comment

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

# seed ratings
Rating.objects.get_or_create(book=book1, user='daniel', defaults={'score': 5})
Rating.objects.get_or_create(book=book1, user='maria', defaults={'score': 4})
Rating.objects.get_or_create(book=book2, user='daniel', defaults={'score': 3})
Rating.objects.get_or_create(book=book2,