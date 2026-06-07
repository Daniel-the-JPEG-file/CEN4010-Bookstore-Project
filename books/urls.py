# urls.py maps URLs to their corresponding view functions
# When a request comes in, Django looks here to find which view to call
from django.urls import path
from . import views

urlpatterns = [
    # POST /books/ - Create a new book
    path('books/', views.create_book, name = 'create_book'),

    # GET /books/<isbn>/ - Get a book by ISBN
    # <str:isbn> means Django will capture whatever is in the URL and pass it to the view as 'isbn'
    path('books/<str:isbn>/', views.get_book, name = 'get_book'),

    # POST /authors/ - Create a new author
    path('authors/', views.create_author, name = 'create_author'),

    # GET /authors/<author_id>/books/ - Get all books by an author
    # <int:author_id> means Django expects a number in the URL and passes it to the view as 'author_id'
    path('authors/<int:author_id>/books/', views.get_books_by_author, name = 'get_books_by_author'),
]