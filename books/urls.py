from django.urls import path
from . import views

urlpatterns = [
    path('genre/<str:genre>/', views.books_by_genre, name='books-by-genre'),
    path('top-sellers/', views.top_sellers, name='top-sellers'),
    path('price/<str:order>/', views.books_by_price, name='books-by-price'),
]