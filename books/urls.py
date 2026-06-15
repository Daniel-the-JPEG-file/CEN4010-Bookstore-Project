from django.urls import path
from . import views

urlpatterns = [
    path('genre/<str:genre>/', views.books_by_genre, name='books-by-genre'),
]