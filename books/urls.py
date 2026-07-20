# urls.py maps URLs to their corresponding view functions
# When a request comes in, Django looks here to find which view to call
from django.urls import path
from . import views  # Used for book/author views
from .views import ( # Used for user/credit card views
    create_user,
    get_user,
    update_user,
    create_credit_card,
    get_credit_cards,
)

urlpatterns = [

    # --- Book & Author Endpoints ---
    # POST /books/ - Create a new book
    path('books/', views.create_book, name='create_book'),

    # YOUR NEW ROUTE HERE:
    path('genre/<str:genre>/', views.books_by_genre),

    # Price Sorting Endpoints
    path('books/price/desc/', views.get_books_by_price_desc),
    path('books/price/asc/', views.get_books_by_price_asc),

    # GET /books/<isbn>/ - Get a book by ISBN
    # <str:isbn> means Django will capture whatever is in the URL and pass it to the view as 'isbn'
    path('books/<str:isbn>/', views.get_book, name='get_book'),

    # POST /authors/ - Create a new author
    path('authors/', views.create_author, name='create_author'),

    # GET /authors/<author_id>/books/ - Get all books by an author
    # <int:author_id> means Django expects a number in the URL and passes it to the view as 'author_id'
    path('authors/<int:author_id>/books/', views.get_books_by_author, name='get_books_by_author'),

    # --- User & Credit Card Endpoints ---
    path("users/create/", create_user),

    path("users/<str:username>/", get_user),

    path("users/<str:username>/update/", update_user),

    path("users/<str:username>/creditcards/", create_credit_card),

    path("users/<str:username>/creditcards/list/", get_credit_cards),
]